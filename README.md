# resize-img

```
usage: main.py [-h] -f F [-o O] -s S [-n N]

Resize images

optional arguments:
  -h, --help  show this help message and exit
  -f F        Mask for input files
  -o O        Output folder
  -s S        Size for resizing, format WхH. Where W and H may be a number
              (for hard resize), float number for procentage resize or "p" for
              the proportional resize
  -n N        New name for files. Can contain formating. For example,
              "image{n}.png" You can use:n -- numberext -- extensionon -- old
              name of fileand other str.format() features
```
## Some examples
```
main.py -f "*.png" -o "imgs/ach/wow" -n "img{n}.{ext}" -s 96x96

main.py -f "*.png" -o "imgs/ach/wow" -n "img{n}.{ext}" -s 96x2.0

main.py -f "*.(png|gif|jpg)" -o "imgs/" -n "{n}_new.{ext}" -s 800xp
```

