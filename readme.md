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

└───projects
    │   .gitignore
    │   readme.md
    │
    ├───packages
    │   ├───package1
    │   │   ├───connectors
    │   │   │       db1_conn.py
    │   │   │
    │   │   ├───queries
    │   │   │       db1_query.py
    │   │   │       query_executor.py
    │   │   │
    │   │   └───transformers
    │   │           db_etl_1.py
    │   │
    │   └───package2
    │       ├───connectors
    │       │       db2_conn.py
    │       │
    │       ├───queries
    │       │       db2_query.py
    │       │       query_executor.py
    │       │
    │       └───transformers
    │               db_etl_2.py
    │
    ├───project1
    │       entrypoint_1.py
    │       __init__.py
    │
    └───project2
            entrypoint_2.py
            __init__.py



</pre>