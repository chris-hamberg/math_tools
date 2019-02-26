'''
Program that prints the output

    * 
   * *
  * * * 
 * * * * 
* * * * *

'''
### NOTE THEORY
'''
The triangle image is inside a 5x9 area. Consider all mxn areas. Given the ith 
row in a 1-based index, i times star-space pairs "* " occur. Also, in the ith 
row, there are (m - i) spaces of leading margin. Thus, given a 5x9 field:
    
    i=5: leading margin (5 - i) = 0, and i=5 times star-space pairs "* "
    i=4: leading margin (5 - i) = 1, and i=4 times star-space pairs "* "
        .
        .
        .
    i=1: leading margin (5 - i) = 4, and i=1 times star-space pairs "* "

In general, in any mxn field, the qth row is:

    i=q: leading margin (m - i), and i times star-space pairs "* "
'''
space, apogaeum = range, 1 # alias

def star_tree(finituma=5):
    for stars in space(apogaeum, finituma+1):
        horizon = -stars + finituma
        print(" "*horizon + "* "*stars)

if __name__ == '__main__':
    star_tree()
