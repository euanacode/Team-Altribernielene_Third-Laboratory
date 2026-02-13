# Team-Altribernielene_Third-Laboratory

Group Members:
Luna, Alyssa Euana
Pabonita, Trisha Aira
Calo, Liberty Case
Beatisula, Nathaniel
Bautista, Chrisa Lene Joy

Analysis Questions <<
Provide concise but well-structured explanations. 

1. Differentiate Task and Data Parallelism. Identify which part of the lab demonstrates each and justify the workload division.
- Task Parallelism involves executing different tasks at the same time using the same data. In Part A, different deduction functions (SSS, PhilHealth, Pag-IBIG, and Tax) were executed concurrently for a single employee salary. Data Parallelism involves performing the same operation on multiple data inputs simultaneously. In Part B, the payroll computation function was applied concurrently to multiple employees.

2. Explain how concurrent.futures managed execution, including submit(), map(), and Future objects. Discuss the purpose of with when creating an Executor. 
- The submit() method schedules individual tasks and returns a Future object that represents the result of asynchronous execution. The map() method applies a function to multiple inputs in parallel. Future objects allow retrieval of results once computation is complete. The with statement ensures that threads or processes are properly created and terminated after execution.


3. Analyze ThreadPoolExecutor execution in relation to the GIL and CPU cores. Did true parallelism occur? 
- ThreadPoolExecutor does not achieve true parallelism for CPU-bound tasks due to Python's Global Interpreter Lock (GIL). Although tasks execute concurrently, only one thread can run Python bytecode at a time. Thus, execution was concurrent but not fully parallel.

4. Explain why ProcessPoolExecutor enables true parallelism, including memory space separation and GIL behavior. 
- ProcessPoolExecutor enables true parallelism by using separate processes. Each process has its own memory space and Python interpreter, allowing execution across multiple CPU cores without GIL limitations.

5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which approach scales better and why? 
- If the number of employees increases from 5 to 10,000, Data Parallelism scales better. ProcessPoolExecutor distributes computations across multiple CPU cores, improving performance for large workloads. Thread-based execution would be limited by the GIL.

6. Provide a real-world payroll system example. Indicate where Task Parallelism and Data Parallelism would be applied, and which executor you would use.
- In a real payroll system: Task Parallelism can be used to compute deductions such as tax, insurance, and benefits simultaneously for one employee. Data Parallelism can be applied to process thousands of employees concurrently. ThreadPoolExecutor is suitable for task-based operations, while ProcessPoolExecutor is ideal for large-scale payroll processing.
