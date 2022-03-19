# Session

```python
# List of extensions supported to convert run arguments into actual fetches and
# feeds.
#
# Each element in the list is a tuple of (Type, fetch_fn, feed_fn1, feed_fn2),
# where the function signatures are:
#   fetch_fn : Type -> (list of Tensors,
#                       lambda: list of fetched np.ndarray -> TypeVal)
#     fetch_function describes how to expand fetch into its component Tensors
#     and how to contract the fetched results back into a single return value.
#   feed_fn1 : Type, TypeVal -> list of (Tensor, value)
#     Each feed function describes how to unpack a single fed value and 
#     map it to feeds of one or more tensors and their corresponding values.
#   feed_fn2 : Type -> list of Tensors
#     A callable for specifying tensor values to feed 
#     when setting up a partial run
_REGISTERED_EXPANSIONS = [ ... ]
class SessionInterface(object):
  """Base class for implementations of TensorFlow client sessions."""
  @property
  def graph(self):
  """The underlying TensorFlow graph, to be used in building Operations."""
   @property
  def sess_str(self):
  """The TensorFlow process to which this session will connect."""
  def run(self, fetches, feed_dict=None, options=None, run_metadata=None):
  """Runs operations in the session. See `BaseSession.run()` for details."""
  def partial_run_setup(self, fetches, feeds=None):
  """Sets up the feeds and fetches for partial runs in the session."""
  def partial_run(self, handle, fetches, feed_dict=None):
  """Continues the execution with additional feeds and fetches."""
    
class _FetchHandler(object):
  """Handler for structured fetches.

  Given a graph, a user-provided structure for fetches, and a feed dict, this
  class takes care of generating a list of tensor names to fetch and op names
  to run for a low level `run()` call.

  Given the results of the low level run call, this class can also rebuild a
  result structure matching the user-provided structure for fetches, but
  containing the corresponding results.
  """
  def fetches(self):
    """Return the unique names of tensors to fetch.

    Returns:
      A list of strings.
    """
    return self._final_fetches

  def targets(self):
    """Return the unique names of ops to run.

    Returns:
      A list of strings.
    """
    return self._targets

  def build_results(self, session, tensor_values):
    """Build results matching the original fetch shape.

    `tensor_values` must be a list of the same length as
    the one returned by `fetches()`, and holding the requested
    fetch values.

    This method builds a struct with the same shape as the original `fetches`
    passed to the constructor, in which the fetches are replaced by their
    fetched value.

    Args:
      session: The enclosing session.  Used for tensor handles.
      tensor_values: List of values matching the list returned by fetches().

    Returns:
      A structure of the same shape as the original `fetches` argument but
        containing tensors or None (for fetched ops).
    """
    full_values = []
    assert len(self._final_fetches) == len(tensor_values)
    i = 0
    j = 0
    for is_op in self._ops:
      if is_op:
        full_values.append(None)
      else:
        # If the fetch was in the feeds, use the fed value, otherwise
        # use the returned value.
        if self._fetches[i] in self._feed_handles:
          # A fetch had a corresponding direct TensorHandle feed. Call eval()
          # to obtain the Tensor value from the TensorHandle.
          value = self._feed_handles[self._fetches[i]].eval()
        else:
          value = self._feeds.get(self._fetches[i])
        if value is None:
          value = tensor_values[j]
          j += 1
        dtype = self._fetch_handles.get(self._fetches[i])
        if dtype:
          full_values.append(session_ops.TensorHandle(value, dtype, session))
        else:
          full_values.append(value)
        i += 1
    assert j == len(tensor_values)
    return self._fetch_mapper.build_results(full_values)
    
class BaseSession(SessionInterface):
  """A class for interacting with a TensorFlow computation.
  The BaseSession enables incremental graph building with inline
  execution of Operations and evaluation of Tensors.
  """
  def __init__(self, target='', graph=None, config=None):
    """Constructs a new TensorFlow session.
    Args:
      target: (Optional) The TensorFlow execution engine to connect to.
      graph: (Optional) The graph to be used. If this argument is None, the
        default graph will be used.
      config: (Optional) ConfigProto proto used to configure the session. If no
        config is specified, the global default will be used. The global default
        can be configured via the tf.config APIs.
    """
      
  def _run(self, handle, fetches, feed_dict, options, run_metadata):
  """Perform either run or partial_run, depending the presence of `handle`."""
    def _feed_fn(feed, feed_val):
      """[LOGOS] Find matching feed_fn for type of given feed."""
      for tensor_type, _, feed_fn, _ in _REGISTERED_EXPANSIONS:
        if isinstance(feed, tensor_type):
          return feed_fn(feed, feed_val)
          
    # Check validity of session.
    ...
          
    # Create request.
    feed_dict_tensor = object_identity.ObjectIdentityDictionary()
    feed_map = {}      
    
    # Validate and process feed_dict.
    feed_handles = {}
    if feed_dict:
      # [LOGOS] flatten a feed_dict of nested tree structure
      # example_dict = {(4, 5, (6, 8)): ("a", "b", ("c", "d"))}
      # flattened = {4: "a", 5: "b", 6: "c", 8: "d"}
      feed_dict = flatten(feed_dict)
      for feed, feed_val in feed_dict.items():
        for subfeed, subfeed_val in _feed_fn(feed, feed_val):
          # assert subfeed is a node of self.graph
          # assert subfeed_val is NOT a tensor
          ...
          subfeed_dtype = subfeed_t.dtype.as_numpy_dtype
          # assert subfeed is feedable
          # try to convert subfeed_val to np array
          is_tensor_handle_feed = isinstance(subfeed_val,
                                             session_ops.TensorHandle)
          if is_tensor_handle_feed:
            np_val = subfeed_val.to_numpy_array()
            feed_handles[subfeed_t] = subfeed_val
          else:
            np_val = np.asarray(subfeed_val, dtype=subfeed_dtype)

          ...
          feed_dict_tensor[subfeed_t] = np_val
          feed_map[compat.as_bytes(subfeed_t.name)] = (subfeed_t, subfeed_val)
    
    # Create a fetch handler to take care of the structure of fetches.
    fetch_handler = _FetchHandler(
    self._graph, fetches, feed_dict_tensor, feed_handles=feed_handles)
    
    # Run request and get response.
    
    # [LOGOS] solve device incompatible problems for tensors and handles
    ...
    
    final_fetches = fetch_handler.fetches()
    final_targets = fetch_handler.targets()
    # We only want to really perform the run if fetches or targets are provided,
    # or if the call is a partial run that specifies feeds.
    if final_fetches or final_targets or (handle and feed_dict_tensor):
      # [LOGOS] This _do_run will really run the core TF session.
      results = self._do_run(handle, final_targets, final_fetches,
                             feed_dict_tensor, options, run_metadata)
    else:
      results = []
    return fetch_handler.build_results(self, results)
```

