# Miscellaneous

```text
docker ps # 显示当前运行的 container
docker imagse # 显示本地保存的所有镜像
```

## Kernel Compatibility Check

https://docs.docker.com/engine/install/troubleshoot/

```bash
$ curl https://raw.githubusercontent.com/docker/docker/master/contrib/check-config.sh > check-config.sh

$ bash ./check-config.sh
```

## Removal of Images

To remove all stopped containers:

```
docker rm  $(docker ps -q -a)
```

ref: https://stackoverflow.com/questions/51188657/image-is-being-used-by-stopped-container

To remove all dangling images (with TAG `<NONE>` ):

```
docker rmi $(docker images -a -f dangling=true -q)
```

ref: https://stackoverflow.com/questions/33913020/docker-remove-none-tag-images

## Rootless Mode

https://docs.docker.com/engine/security/rootless/