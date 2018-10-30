# Staff

This is the GPT partition table for one of my machines that i've edited
to have a red herring key in the first 512 bytes, but the real key is the
name of the second partition, retrievable with `gdisk`, as shown:

```
Number  Start (sector)    End (sector)  Size       Code  Name
   1            2048         1128447   550.0 MiB   EF00  
   2         1128448         5322751   2.0 GiB     8200  Linux swap
   3         5322752        57751551   25.0 GiB    8304  this_is_the_flag!

   4        57751552       500118158   210.9 GiB   8302  Linux /home
```
