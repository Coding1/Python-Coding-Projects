#!/usr/bin/python
# https://imagineer.in/blog/an-attempt-to-implement-rsa/
import json, sys, hashlib, math
from fractions import gcd

def usage():
    print """Usage:
    python find_waldo.py student_id (i.e., qchenxiong3)"""
    sys.exit(1)
    
def gcd(w, m):
    while m != 0:
        w, m = m, w % m
    return w


# Function to compute the prime factors of n
# prime factorization brute-force algorithm

#TODO -- n1 and n2 share p or q?
# Compute prime factors of n1 
def is_waldo(n1, n2):
    #your code start here
    n1 = n1**0.5
    n2 = n2**0.5
    result = False
    i = 2  
    factors_n1 = [] 
    
    while i * i <= n1:
        if n1 % i:
            i += 1
        else:
            n1 //= i
            factors_n1.append(i)
    if n1 > 1:
        factors_n1.append(n1)
        #print "The factors of n: ", factors_n1
        
    p = factors_n1[0] 
    q = factors_n1[1] 
    
    #print("Value of n1 p : "  , p)
    #print("Value of n1 q : "  , q)  
    
    #Compute the prime factors of n2
    j = 2  
    factors_n2 = [] 
    
    while j * j <= n2:
        if n2 % j:
            j += 1
        else:
            n2 //= j
            factors_n2.append(j)
    if n2 > 1:
        factors_n2.append(n2)
        #print "The factors of n: ", factors_n2
        
    p = factors_n2[0] 
    q = factors_n2[1] 
    
    #print("Value of n2 p : "  , p)
    #print("Value of n2 q : "  , q)  
    
    if factors_n1 in factors_n2:
        result = True
    else:
        result = False
    
        return factors_n1, factors_n2          
         
           
     
    #your code ends here

    return result

#TODO -- get private key of n1
def get_private_key(n1, n2, e):
    d = 0 
    #phi_1 = 0
    #phi_2 = 1
    #phi_3 = 1
    n1 = n1**0.5
    n2 = n2**0.5    

    #your code starts here
    # Function to compute the prime factors of n1
    # prime factorization brute-force algorithm
   
    i = 2  
    factors_n1 = [] 
    
    while i * i <= n1:
        if n1 % i:
            i += 1
        else:
            n1 //= i
            factors_n1.append(i)
    if n1 > 1:
        factors_n1.append(n1)
        #print "The factors of n: ", factors_n1
        
    p = factors_n1[0] 
    q = factors_n1[1] 
    
    #print("Value of n1 p : "  , p)
    #print("Value of n1 q : "  , q)       
    
    # your code starts here    
    # Compute p & q prime status     
    n = p * q    
    #print("Value of n: ", n)

    #Compute phi totient of n
    phi = (p-1) * (q-1)
    #print("Value of phi : ", phi)

    #Choose an integer e such that e and phi(n) are coprime    

    # Confirm coprimes with Euclid's Algorithm  - e and phi(n) 
    co_primes = (e, phi)
    while co_primes != 1:        
        co_primes = gcd(e, phi)
        #print("Check value of e and phi for co primes: ", co_primes)
        
    # multiplicative inverse calculation
    # multiplicative inverse
    phi_value = phi
    exponent = e
    
    d = e**(-1)%(phi_value)
    #print("Test point phi: ", p)
    
    '''while exponent > 0:
        phi_a = phi_value/exponent 
        phi_b = phi_value - phi_a * exponent 
        phi_value = exponent 
        exponent = phi_b 
        
        x_phi = phi_2 - phi_a * phi_1
        y_phi = d - phi_a * phi_3
        
        phi_2 = phi_1
        phi_1 = x_phi
        d = phi_3
        phi_3 = y_phi
    
    if phi_value == 1:
        return d + phi'''


    #Check if phi equals 1
    #d = (e, phi)  
    d = int('d', 16) 

    #your code ends here

    return d

def main():
    if len(sys.argv) != 2:
        usage()

    all_keys = None
    with open("keys4student.json", 'r') as f:
        all_keys = json.load(f)

    name = hashlib.sha224(sys.argv[1].strip()).hexdigest()
    if name not in all_keys:
        print sys.argv[1], "not in keylist"
        usage()

    pub_key = all_keys[name]
    n1 = int(pub_key['N'], 16)
    e = int(pub_key['e'], 16)
    d = 0
    waldo = "dolores"

    print "your public key: (", hex(n1).rstrip("L"), ",", hex(e).rstrip("L"), ")"

    for classmate in all_keys:
        if classmate == name:
            continue
        n2 = int(all_keys[classmate]['N'], 16)

        if is_waldo(n1, n2):
            waldo = classmate
            d = get_private_key(n1, n2, e)
            break
    
    print "your private key: ", hex(d).rstrip("L")
    print "your waldo: ", waldo


if __name__ == "__main__":
    main()
