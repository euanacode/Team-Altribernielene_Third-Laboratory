from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import time


# Define individual deduction functions
def compute_sss(salary):
    """
    Compute SSS deduction (4.5% of salary)
    
    Args:
        salary: Employee's gross salary
    
    Returns:
        Tuple of (deduction_name, amount, thread_name)
    """
    time.sleep(0.1)  # Simulate I/O operation
    deduction = salary * 0.045
    thread_name = threading.current_thread().name
    return ("SSS", deduction, thread_name)


def compute_philhealth(salary):
    """
    Compute PhilHealth deduction (2.5% of salary)
    
    Args:
        salary: Employee's gross salary
    
    Returns:
        Tuple of (deduction_name, amount, thread_name)
    """
    time.sleep(0.1)  # Simulate I/O operation
    deduction = salary * 0.025
    thread_name = threading.current_thread().name
    return ("PhilHealth", deduction, thread_name)


def compute_pagibig(salary):
    """
    Compute Pag-IBIG deduction (2% of salary)
    
    Args:
        salary: Employee's gross salary
    
    Returns:
        Tuple of (deduction_name, amount, thread_name)
    """
    time.sleep(0.1)  # Simulate I/O operation
    deduction = salary * 0.02
    thread_name = threading.current_thread().name
    return ("Pag-IBIG", deduction, thread_name)


def compute_withholding_tax(salary):
    """
    Compute Withholding Tax (10% of salary)
    
    Args:
        salary: Employee's gross salary
    
    Returns:
        Tuple of (deduction_name, amount, thread_name)
    """
    time.sleep(0.1)  # Simulate I/O operation
    deduction = salary * 0.10
    thread_name = threading.current_thread().name
    return ("Withholding Tax", deduction, thread_name)


def compute_deductions_task_parallel(employee_name, salary):
    """
    Compute all deductions for a single employee using Task Parallelism
    
    Args:
        employee_name: Name of the employee
        salary: Employee's gross salary
    
    Returns:
        Dictionary containing all deduction details
    """
    print(f"\n{'='*60}")
    print(f"TASK PARALLELISM - Computing deductions for {employee_name}")
    print(f"Gross Salary: ₱{salary:,.2f}")
    print(f"{'='*60}\n")
    
    # List of deduction functions to execute
    deduction_functions = [
        compute_sss,
        compute_philhealth,
        compute_pagibig,
        compute_withholding_tax
    ]
    
    # Dictionary to store results
    deductions = {}
    total_deduction = 0
    
    # Use ThreadPoolExecutor for concurrent task execution
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Submit all tasks and get Future objects
        futures = {
            executor.submit(func, salary): func.__name__ 
            for func in deduction_functions
        }
        
        # Retrieve results as they complete
        for future in as_completed(futures):
            deduction_name, amount, thread_name = future.result()
            deductions[deduction_name] = amount
            total_deduction += amount
            
            print(f"  {deduction_name:<18} : ₱{amount:>10,.2f}  [Thread: {thread_name}]")
    
    # Calculate net salary
    net_salary = salary - total_deduction
    
    print(f"\n{'-'*60}")
    print(f"  {'Total Deductions':<18} : ₱{total_deduction:>10,.2f}")
    print(f"  {'Net Salary':<18} : ₱{net_salary:>10,.2f}")
    print(f"{'-'*60}")
    
    return {
        'employee': employee_name,
        'gross_salary': salary,
        'deductions': deductions,
        'total_deduction': total_deduction,
        'net_salary': net_salary
    }


def main():
    """
    Main function to demonstrate Task Parallelism
    """
    print("\n" + "="*60)
    print("PART A: TASK PARALLELISM DEMONSTRATION")
    print("="*60)
    
    # Test with one employee
    employee_name = "Alice"
    salary = 25000
    
    start_time = time.time()
    result = compute_deductions_task_parallel(employee_name, salary)
    end_time = time.time()
    
    print(f"\n{'='*60}")
    print(f"Execution completed in {end_time - start_time:.4f} seconds")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()