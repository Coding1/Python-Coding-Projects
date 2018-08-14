#!/usr/bin/python
import json, sys, hashlib

def usage():
    print """Usage:
        python get_pri_key.py student_id (i.e., qchenxiong3)"""
    sys.exit(1)

# TODO -- get n's factors
# reminder: you can cheat ;-), as long as you can get p and q

# Function to compute the gcd(a,b), is the largest integer that divides (without remainder) both a and b.
# Function to compute GCD
def gcd(w, m):
    while m != 0:
        w, m = m, w % m
    return w

# Function to compute the prime factors of n
# prime factorization brute-force algorithm 
def get_factors(n):   

    # your code starts here
    i = 2  
    factors_n = [] 
    
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors_n.append(i)
    if n > 1:
        factors_n.append(n)
        #print "The factors of n: ", factors_n
        
    p = factors_n[0] 
    q = factors_n[1] 
    
    #print("Value of p : "  , p)
    #print("Value of q : "  , q)        
           
    # Calculate n based on  p * q
    n = p * q    
    #print("Value of n = p * q : ", n)  
   
    # your code ends here
    return (p, q)

# TODO: write code to get d from p, q and e
def get_key(p, q, e):
    d = 0     
    phi_1 = 0
    phi_2 = 1
    phi_3 = 1       
    
    # your code starts here    
    # Compute p & q prime status    
    n = p * q
    #print("Value of n: ", n)

    #Compute phi totient of n
    phi = (p-1) * (q-1)
    #print("Value of phi : ", phi)    

    # Confirm coprimes with Euclid's Algorithm  - e and phi(n) 
    co_primes = (e, phi)
    while co_primes != 1:        
        co_primes = gcd(e, phi)
        
    # multiplicative inverse calculation     
    phi_value = phi
    exponent = e
    
    while exponent > 0:
        phi_a = phi_value/exponent 
        phi_b = phi_value - phi_a * exponent 
        phi_value = exponent 
        exponent = phi_b 
        
        create_phi = phi_2 - phi_a * phi_1
        create_phi_1 = d - phi_a * phi_3
        
        phi_2 = phi_1
        phi_1 = create_phi
        d = phi_3
        phi_3 = create_phi_1
    
    if phi_value == 1:
        return d + phi


    #Use Extended Euclid's Algorithm 
    d = (e, phi)   
   
    #d = hex('d', 16) 
    #print("Value of d: ", d)  
    # your code ends here
    return d

def main():
    if len(sys.argv) != 2:
        usage()

    n = 0
    e = 0

    all_keys = None
    with open("keys4student.json", 'r') as f:
        all_keys = json.load(f)
    
    name = hashlib.sha224(sys.argv[1].strip()).hexdigest()
    if name not in all_keys:
        print sys.argv[1], "not in keylist"
        usage()
    
    pub_key = all_keys[name]
    n = int(pub_key['N'], 16)
    e = int(pub_key['e'], 16)

    print "your public key: (", hex(n).rstrip("L"), ",", hex(e).rstrip("L"), ")"

    (p, q) = get_factors(n)
    d = get_key(p, q, e)
    print "your private key:", hex(d).rstrip("L")

if __name__ == "__main__":
    main()
