# 3.2.5 Compound Commands

* for loop

```bash
# iterate on a series of values
for i in 1 2 3 4 5
do
    echo ${i}
done

# iterate on output lines of a command
for i in $(command)
do

done

# for bash v3.0+: iterate on sequence
for i in {1..5}
do
done

# for bash v4.0+: iterate on sequence by a given step
for i in {1..10..2}
do
  echo "what $i"
done
# output:
# what 1
# what 3
# what 5
# what 7
# what 9
```

* [https://www.cyberciti.biz/faq/bash-for-loop/](https://www.cyberciti.biz/faq/bash-for-loop/)

