# rsync

Usually you do `rsync -a src/ dst` to sync the content of `src` and `dst`. Without the `/` it would put `src` inside `dst` so it becomes `dst/src/...`. Just choose the corresponding form you need.

To sync to/from a remote directory, just do it like `scp`:

```
rsync -a src user@host:dst
rsync -a user@host:src dst 
```

ref: https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories
