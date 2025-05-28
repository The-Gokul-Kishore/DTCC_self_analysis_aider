---

## 🎯 Goal: You want `pgvector` running inside Docker on your computer.

Let’s do this in **5 simple baby steps**. Don’t think ahead. Just follow one at a time. Ready?

---
# how to download pg Vector after installing docker
## ✅ STEP 1: Open Command Prompt

1. Press `Windows` key
2. Type `cmd`
3. Hit `Enter`

Done? Good.

---

## ✅ STEP 2: Pull the pgvector Docker

Type this in the Command Prompt:

```bash
docker pull ankane/pgvector
```

🕐 This downloads pgvector for PostgreSQL. Wait till it finishes.

---

## ✅ STEP 3: Start the pgvector database

Now run this:

```bash
docker run --name pgvector-db -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=vector_db -p 5432:5432 -d ankane/pgvector
```

👉 This means:

* Your database is called `vector_db`
* Your username is `admin`
* Your password is `admin`

---

## ✅ STEP 4: Go inside the database

Now run this:

```bash
docker exec -it pgvector-db psql -U admin -d vector_db
```

You are now **inside** the PostgreSQL database!

---

## ✅ STEP 5: Turn on `pgvector` feature

Type this **exactly**:

```sql
CREATE EXTENSION vector;
```

Then hit `Enter`.

You’ll see:

```
CREATE EXTENSION
```

You just enabled `pgvector`. 🧠🔥

Now type:

```sql
\q
```

That exits the database.

---

## 🎉 You did it!

That’s all. No magic. No errors. You now have a working PostgreSQL database with vector search.

---

If you're ready for the next step (like adding data or running a project with it), just say:

**“Next step”**

Or if you're stuck at any step, just copy-paste what went wrong — I’ll help **without judgment**. You're doing amazing.
