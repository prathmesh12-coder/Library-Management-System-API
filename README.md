# Library Management System API

## Technologies Used

- FastAPI
- Pydantic
- MongoDB (via PyMongo)

Welcome to the Library Management System API! This API allows you to manage students' information in a library system.

## Endpoints

### Create a New Student

**URL:** `POST /api/students`

**Description:** Creates a new student record in the system.

**Request Body:**
```json
{
    "name": "John Cena",
    "age": 100,
    "address": {
        "city": "Seattle",
        "country": "USA"
    }
}
```
**Response:**
```json
{
    "id": "6613ee26ec68e9da034ef06f"
}
```

### List Students

**URL:** `GET /api/students`

**Description:** Retrieves a list of students from the system, with optional filtering by country and age.

**Query Parameters:**
+ `country` (optional): Filter students by country.
+  `age` (optional): Fliter students by age.

**Response:**
```json
{
    "data": [
        {
            "name": "John Cena",
            "age": 100
        },
        {
            "name": "Serena Williams",
            "age": 39
        },
        {
            "name": "Usain Bolt",
            "age": 35
        }
    ]
}

```

### Get Student by ID

**URL:** `GET /api/students/{id}`

**Description:** Retrieves details of a specific student by their ID.

**Path Parameter:** 
+ `id`: ID of the student to retrieve.

**Response:**
```json
{
    "name": "John Cena",
    "age": 100,
    "address": {
        "city": "Seattle",
        "country": "USA"
    }
}
```

### Update Student

**URL:** `PATCH /api/students/{id}`

**Description:** Updates information for a specific student by their ID.

**Path Paremeter:**

+ `id`:ID of the student to update.

**Request Body(Partial Update):**
```json
{
    "name": "John Cena Jr."
}
```

**Response:** `104 No Content`

### Delete Student

**URL:** `DELETE /api/students/{id}`

**Description:** Deletes a specific student by their ID.

**Path Parameter:**
+ `id`:ID of the student to delete.

**Response:**
```json
{
    "message": "Student deleted successfully"
}
```









