# Use the find_root function:
def find_root(x, power, epsilon):
        if x<0 and power %2==0:
                return None #Negative number has no even-power roots
        low = min (-1,x)
        high = max(1,x)
        #Use bisection search
        ans = (high + low)/2
        while abs(ans**power - x) >= epsilon:
                if ans**power <x:
                        low = ans
                else:
                        high = ans 
                ans= (high+low)/2 
        return ans 
# 
# 
# 
# 
# 
# to print
# the sum of approximations to the square root of 25, the cube root of
# -8, and the fourth root of 16. Use 0.001 as epsilon.
def test_find_root(x_vals, powers, epsilons):
        for x in x_vals:
                for p in powers:
                        for e in epsilons:
                                result= find_root(x, p, e)
                                if result == None:
                                        val = ' No roots exists'
                                else:
                                        val = 'Okay'
                                        if abs(result**p - x)>e:
                                                val='Bad'
                                print(f'x={x}, power ={p}, epsilon ={e}: {val}')


x_vals = (0.25, 8, -8)
powers = (1,2,3)
epsilons= (0.1, 0.001, 1)
test_find_root(x_vals, powers, epsilons)

# 
# 
# 
# 
# 
# to print
# the sum of approximations to the square root of 25, the cube root of
# -8, and the fourth root of 16. Use 0.001 as epsilon.

