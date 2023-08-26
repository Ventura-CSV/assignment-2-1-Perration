def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    #Total number of students
    #40 males
    #60 females
   
    males = int(input("Enter number of males: "))  
    females = int(input("Enter number of females: ")) 
    total_students = males + females  
    
    m_perc = males / total_students * 100
    f_perc = females / total_students * 100
    
    print("The total number of students: " + str(total_students)) 
    print(f"The number of males and females: \t {(males)} \t {(females)}")
    print(f'The percentage of males and females: \t {m_perc:.2f} \t {f_perc:.2f}') 
    
    """    
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
