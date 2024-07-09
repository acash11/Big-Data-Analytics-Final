#pip install rbloom
from rbloom import Bloom
bf = Bloom(200, 0.01)  # 200 items max, false positive rate of 1%
bf.add((12, 1))

print((12, 1) in bf)

print("world" in bf)

bf.update(["hello", "world"])  # "hello" and "world" now in bf
other_bf = Bloom(200, 0.01)

### add some items to other_bf

third_bf = bf | other_bf    # third_bf now contains all items in
                            # bf and other_bf
third_bf = bf.copy()
third_bf.update(other_bf)   # same as above
print(bf.issubset(third_bf))    # bf <= third_bf also works
