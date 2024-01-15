import math
import numpy as np
import matplotlib.pyplot as plt

q_z = 1
v_z0 = 0
dt = 0.017

x0 = 0
y0 = 0 
x_f = 1
y_f = 1 
v_x0 = -0.2 
v_y0 = 0.5



#calculates q_bar
def q_calc(z_f,v_z0,q_bar):
    c = v_z0 - z_f
    return q_bar*np.sign(v_z0/q_bar - np.sign(c)*(math.e**np.abs(c/q_bar) - 1))

#calculates t_f
def t_f_calc(z_f,v_z0,q_bar):

    c = v_z0 - z_f
    q_z = q_calc(z_f,v_z0,q_bar)
    
    D = 1 + math.e**(c/q_z)*(v_z0/q_z - 1)
    t2 = np.log(1 + math.sqrt(D))   
    
    t1 = t2 -c/q_z
    
    
    return t1+t2


def validate_interval(y):
    return y< 0


# solve for root using bisection method
def bisection(x_f,v_x,y_f,v_y, t_f_calc, interval, tol):

    # extract interval start and end points
    x0, x1 = interval[0], interval[1]

    # check interval can be used to solve for root
    # if not validate_interval(t_f_calc, x0, x1):
    #     return

    # iterations required to find the root within a specified error bound
    n = error_bound(x0, x1, tol)

    counter = 1

    # iterate over error bound
    while True:

        # calculate root approximation
        root_approx = x0 + ((x1 - x0) / 2)
        root_approx_y = math.sqrt(1-root_approx**2)
        # evaluate y at current estimate
        
        y = t_f_calc(x_f,v_x,root_approx) - t_f_calc(y_f,v_y,root_approx_y)
        print(root_approx, root_approx_y)
        # check tolerance condition
        if -tol < y < tol:
            # check that error bound actually worked
            print(counter, n)
           

            # return root approximation
            return root_approx

        # check if next segment is left of bisection
        if validate_interval(y):
            x1 = root_approx
        else:
            x0 = root_approx

        # increment counter
        counter += 1

def error_bound(a, b, err):
    n = np.log((b - a) / err) / np.log(2)
    return int(np.ceil(n))

def main():
    print("Hello World!")
    
    t = 0
    interval = [0,1] 
    
    x = [x0]
    y = [y0]
    v_x = v_x0
    v_y = v_y0
    x_f_new = x_f
    # calculating q_bar
    q_bar = bisection(x_f_new, v_x,y_f,v_y, t_f_calc, interval, dt)
    # calculating t_f
    t_f = t_f_calc(x_f,v_x0,q_bar)

    c = v_x - x_f
    time = [t]
    q_x = q_calc(x_f_new,v_x,q_bar) # calculating q_x
    q_y = math.sqrt(1-q_x**2) # calculating q_y
    t1 = (t_f-c/q_x)/2 # calculating t_1
    q_x_array = [q_x] 
    q_y_array = [q_y]
  
    while t <= t1:
        x.append(math.e**(-t)*(q_x - v_x) + q_x*(t-1) + v_x)
        y.append(math.e**(-t)*(q_y - v_y) + q_y*(t-1) + v_y)
        q_x_array.append(q_x)
        q_y_array.append(q_y)
        t += dt
        time.append(t)
    q_x = -q_x
    q_y = -q_y
    while t<=t_f:
        x.append(-q_x*(t_f - t - math.e**(t_f -t) + 1) + x_f)
        y.append(-q_y*(t_f - t - math.e**(t_f -t) + 1) + y_f)
        q_x_array.append(q_x)
        q_y_array.append(q_y)
        t += dt
        time.append(t)


    
    plt.plot(x,y,'r')

    # Uncomment the below lines to view q vs t plot
    # plt.plot(time,q_y_array,'r')
    # plt.plot(time,q_x_array,'r')

if __name__ == "__main__":
    main()
plt.show()