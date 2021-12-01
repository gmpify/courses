import scala.beans.BeanProperty

class Student(@BeanProperty var name: String, @BeanProperty var id: Long)

val s = new Student("Gabriel", 33)

println(s.getName)
println(s.getId)

s.setName("Gabriel Parreiras")

println(s.getName)

// :javap Student

// Scala methods
// public java.lang.String name();
// public void name_$eq(java.lang.String);
// public long id();
// public void id_$eq(long);

// Java methods
// public long getId();
// public java.lang.String getName();
// public void setId(long);
// public void setName(java.lang.String);
