This is a handy tool for doing some simple media manipulations.

## Screen Recording

See ref for further info. 

For Windows, you need a DirectShow device, which can be installed from [here](https://github.com/rdp/screen-capture-recorder-to-video-windows-free/releases):

```
ffmpeg -f dshow -i video="screen-capture-recorder" output.mkv
```

ref:
[1] https://trac.ffmpeg.org/wiki/Capture/Desktop
[2] https://trac.ffmpeg.org/wiki/DirectShow
[3] https://github.com/rdp/screen-capture-recorder-to-video-windows-free/releases