# Template for modular-polyrepo software design patterns
---

## Modularity: 
### Each package within the Packages directory represents a modular component with specific functionality. This follows the modular design principle where components are self-contained and reusable.
#### ref: https://en.wikipedia.org/wiki/Modular_programming

## Polyrepo: 
### Each project resides in its own repository. This offers the benefits of separate version control, isolation, and scalability for each project.
#### ref: https://webo.digital/blog/monorepo-vs-polyrepo-architecture/


---

### Project structure




<pre>
├───packages
│   ├───package1
│   │   ├───connectors
│   │   │   │   db1_conn.py
│   │   │   │
│   │   │   └───__pycache__
│   │   │           db1_conn.cpython-39.pyc
│   │   │
│   │   ├───queries
│   │   │   │   db1_query.py
│   │   │   │   query_executor.py
│   │   │   │
│   │   │   └───__pycache__
│   │   │           db1_query.cpython-39.pyc
│   │   │           query1.cpython-39.pyc
│   │   │           query_executor.cpython-39.pyc
│   │   │
│   │   └───transformers
│   │       │   db_etl_1.py
│   │       │
│   │       └───__pycache__
│   │               db_etl_1.cpython-39.pyc
│   │
│   └───package2
├───project1
│   │   main.py
│   │   __init__.py
│   │
│   └───__pycache__
│           __init__.cpython-39.pyc
│
└───project2
        main.py
        __init__.py
</pre>