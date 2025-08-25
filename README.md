# File structure (N-Tier Architecture)
```
library_system/
│── models/
│   ├── base.py
│   ├── book.py
│   ├── library.py
│   ├── librarian.py
│   ├── member.py
│   ├── student.py
│   └── teacher.py
│
│── repositories/
│   ├── base_repository.py
│   ├── book_repository.py
│   ├── library_repository.py
│   ├── librarian_repository.py
│   ├── member_repository.py
│
│── services/
│   ├── book_service.py
│   ├── library_service.py
│   ├── librarian_service.py
│   ├── member_service.py
│
│── schema.sql
│── db_init.py
│── main.py 

```

<p>Authentication logic</p>

<span> Create an Auth Service</span>