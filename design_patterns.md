# Python Design Patterns


## Object-oriented analysis (OOA)

This is the process of looking at a problem, system, or task (that somebody wants to turn into an application) and identifying the objects and interactions between those objects. The analysis stage is all about what needs to be done. The output of the analysis stage is a set of requirements. If we were to complete the analysis stage in one step, we would have turned a task, such as, I need a website, into a set of requirements. For example:

Website visitors need to be able to (*italic* represents actions, **bold** represents objects):
- *review* our **history**
- *apply* for **jobs**
- *browse, compare,* and *order* **products**

In software development, the initial stages of analysis include interviewing customers, studying their processes, and eliminating possibilities.

## Object-oriented design (OOD)

This is the process of converting such requirements into an implementation specification. The designer must name the objects, define the behaviors, and formally specify which objects can activate specific behaviors on other objects. The design stage is all about how things should be done. The output of the design stage is an implementation specification. If we were to complete the design stage in a single step, we would have turned the requirements defined during object-oriented analysis into a set of classes and interfaces that could be implemented in (ideally) any object-oriented programming language.

There is a great [designing tool here](http://ondras.zarovi.cz/sql/demo).

Identifying objects is a very important task, but it isn't always as easy as counting the nouns in a short paragraph.

> Remember, class objects are things that have both data and behavior. If we are working only with data, we are often better off storing it in a list, set, dictionary, or some other Python data structure . On the other hand, if we are working only with behavior, but no stored data, a simple function is more suitable.

## Object-oriented programming (OOP)

This is the process of converting the defined design into a working program.

Most twenty-first century development happens in an iterative development model. In iterative development, a small part of the task is modeled, designed, and programmed, then the program is reviewed and expanded to improve each feature and include new features in a series of short development cycles.

## Unified Modeling Language (UML)

A general-purpose, developmental, modeling language in the field of software engineering, that is intended to provide a standard way to visualize the design of a system.

## Manager Objects

Higher-level objects that manage other objects. These are the objects that tie everything together. Analogously, the attributes on a management class tend to refer to other objects that do the "visible" work; the behaviors on such a class delegate to those other classes at the right time, and pass messages between them.





# Database Relationships

## One to Many

Using the example of a microblog, the two entities linked by this relationship are users and posts. A user has many posts, and a post has one user (or author). The relationship is represented in the database with the use of a foreign key on the "many" side. In the relationship below, the foreign key is the user_id field added to the posts table. This field links each post to the record of its author in the user table.

```
class User(db.Model):
    # ...
    id = db.Column(db.Integer, primary_key=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

class Post(db.Model):
    # ...
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
```

It is pretty clear that the user_id field provides direct access to the author of a given post, but what about the reverse direction? For the relationship to be useful I should be able to get the list of posts written by a given user. The user_id field in the posts table is also sufficient to answer this question, as databases have indexes that allow for efficient queries such us "retrieve all posts that have a user_id of X".

## Many to Many

A many-to-many relationship is a bit more complex. As an example, consider a database that has students and teachers. I can say that a student has many teachers, and a teacher has many students. It's like two overlapped one-to-many relationships from both ends. For a relationship of this type I should be able to query the database and obtain the list of teachers that teach a given student, and the list of students in a teacher's class. This is actually non-trivial to represent in a relational database, as it cannot be done by adding foreign keys to the existing tables.

The representation of a many-to-many relationship requires the use of an auxiliary table called an association table (also called a joining table or bridging table). This new table stores two columns, neither of which are primary keys but are linked (foreign-keyed) to the primary keys from the other tables.
```
student_id  teacher_id
s1          t3
s1          t7
s1          t8
s2          t2
s2          t3
s2          t8
s3          t1
s3          t7
```

In the example of tracking users (followers and following), the two entities in the linked relationship instances of the same class. This situation is called a *self-referential relationship.* In the association table, the foreign keys are both pointing to entries in the user table. Each record in this table represents one link between a follower user and a followed user:

```
follower_id  followed_id
u1           u2
u2           u1
u3           u1
u3           u2
u4           u1
```

## Many-to-One

A many-to-one is similar to a one-to-many relationship. The difference is that this relationship is looked at from the "many" side.

##  One-to-One

A one-to-one relationship is a special case of a one-to-many. The representation is similar, but a constrain is added to the database to prevent the "many" side to have more than one link. While there are cases in which this type of relationship is useful, it isn't as common as the other types.
