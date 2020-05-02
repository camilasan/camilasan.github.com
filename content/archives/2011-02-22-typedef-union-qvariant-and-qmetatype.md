
author: Camila
categories: Archives, KDE, poo, Programming
date: "2011-02-22T19:31:35Z"
 
published: true
status: publish
tags: cpp, kde, plugin, quanta
title: typedef, union, QVariant and QMetatype.


<p>Just some notes about typedef, union, QVariant e QMetatype:</p>
<p><strong>typedef</strong>: allow the definition of our own types based on other existing data types.</p>
<p>typedef existing_type new_type_name;</p>
<p>typedef does not create a new type. It only create synonyms of a existing type.</p>
<p><strong>union</strong>: allow one same portion of memory to be acessed as different data types, since all of them are in fact the same location in memory.</p>
<p>union union_name {<br />
member_type1  member_name1;<br />
member_type2 member_name2;<br />
member_type3 member_name3;<br />
member_type4 member_name4;<br />
} object_names;</p>
<p>All the elemenst of the union declaration occupy the same physical space in memory. Its size is the one or the greatest. We can not store different values them independent of each other.</p>
<p><strong>QVariant</strong>: the QVariant class acts like a union for the most common Qt Data types.</p>
<p>C++ forbids unions from including types that have non-defaults constructor or destructor.</p>
<p>A QVariant objects holds a single value of a single type at time.</p>
<p><strong>QMetatype</strong>: It associates a type name to a type, so that it can be created and destructed dynamically at runtime.</p>
<p>Declare Q_DECLARE_METATYPE(type) to make them avaliable to QVariant.</p>
<p><strong>QString</strong>, <strong> QByteArray</strong> and <strong>QVariant</strong> are three classes that have many things in common with containers and that can be used as alternatives to containers in some context. Also like the containers, these classes use implicit sharing as memory and speed optmization.</p>
<p>Fonts:<br />
<a href="http://doc.qt.nokia.com" target="_blank">doc.qt.nokia.com</a><br />
<a href="http://www.cplusplus.com" target="_blank">www.cplusplus.com</a><br />
…........................................................................................................................</p>,-
author: Camila
categories: Archives, KDE, poo, Programming
date: "2011-02-22T19:31:35Z"
 
published: true
status: publish
tags: cpp, kde, plugin, quanta
title: typedef, union, QVariant and QMetatype.


<p>Just some notes about typedef, union, QVariant e QMetatype:</p>
<p><strong>typedef</strong>: allow the definition of our own types based on other existing data types.</p>
<p>typedef existing_type new_type_name;</p>
<p>typedef does not create a new type. It only create synonyms of a existing type.</p>
<p><strong>union</strong>: allow one same portion of memory to be acessed as different data types, since all of them are in fact the same location in memory.</p>
<p>union union_name {<br />
member_type1  member_name1;<br />
member_type2 member_name2;<br />
member_type3 member_name3;<br />
member_type4 member_name4;<br />
} object_names;</p>
<p>All the elemenst of the union declaration occupy the same physical space in memory. Its size is the one or the greatest. We can not store different values them independent of each other.</p>
<p><strong>QVariant</strong>: the QVariant class acts like a union for the most common Qt Data types.</p>
<p>C++ forbids unions from including types that have non-defaults constructor or destructor.</p>
<p>A QVariant objects holds a single value of a single type at time.</p>
<p><strong>QMetatype</strong>: It associates a type name to a type, so that it can be created and destructed dynamically at runtime.</p>
<p>Declare Q_DECLARE_METATYPE(type) to make them avaliable to QVariant.</p>
<p><strong>QString</strong>, <strong> QByteArray</strong> and <strong>QVariant</strong> are three classes that have many things in common with containers and that can be used as alternatives to containers in some context. Also like the containers, these classes use implicit sharing as memory and speed optmization.</p>
<p>Fonts:<br />
<a href="http://doc.qt.nokia.com" target="_blank">doc.qt.nokia.com</a><br />
<a href="http://www.cplusplus.com" target="_blank">www.cplusplus.com</a><br />
…........................................................................................................................</p>
<p>With these notes I intend to finish some new features in my plugin for Quanta :)</p>,-
author: Camila
categories: Archives, KDE, poo, Programming
date: "2011-02-22T19:31:35Z"
 
published: true
status: publish
tags: cpp, kde, plugin, quanta
title: typedef, union, QVariant and QMetatype.


<p>Just some notes about typedef, union, QVariant e QMetatype:</p>
<p><strong>typedef</strong>: allow the definition of our own types based on other existing data types.</p>
<p>typedef existing_type new_type_name;</p>
<p>typedef does not create a new type. It only create synonyms of a existing type.</p>
<p><strong>union</strong>: allow one same portion of memory to be acessed as different data types, since all of them are in fact the same location in memory.</p>
<p>union union_name {<br />
member_type1  member_name1;<br />
member_type2 member_name2;<br />
member_type3 member_name3;<br />
member_type4 member_name4;<br />
} object_names;</p>
<p>All the elemenst of the union declaration occupy the same physical space in memory. Its size is the one or the greatest. We can not store different values them independent of each other.</p>
<p><strong>QVariant</strong>: the QVariant class acts like a union for the most common Qt Data types.</p>
<p>C++ forbids unions from including types that have non-defaults constructor or destructor.</p>
<p>A QVariant objects holds a single value of a single type at time.</p>
<p><strong>QMetatype</strong>: It associates a type name to a type, so that it can be created and destructed dynamically at runtime.</p>
<p>Declare Q_DECLARE_METATYPE(type) to make them avaliable to QVariant.</p>
<p><strong>QString</strong>, <strong> QByteArray</strong> and <strong>QVariant</strong> are three classes that have many things in common with containers and that can be used as alternatives to containers in some context. Also like the containers, these classes use implicit sharing as memory and speed optmization.</p>
<p>Fonts:<br />
<a href="http://doc.qt.nokia.com" target="_blank">doc.qt.nokia.com</a><br />
<a href="http://www.cplusplus.com" target="_blank">www.cplusplus.com</a><br />
…........................................................................................................................</p>,-
author: Camila
categories: Archives, KDE, poo, Programming
date: "2011-02-22T19:31:35Z"
 
published: true
status: publish
tags: cpp, kde, plugin, quanta
title: typedef, union, QVariant and QMetatype.


<p>Just some notes about typedef, union, QVariant e QMetatype:</p>
<p><strong>typedef</strong>: allow the definition of our own types based on other existing data types.</p>
<p>typedef existing_type new_type_name;</p>
<p>typedef does not create a new type. It only create synonyms of a existing type.</p>
<p><strong>union</strong>: allow one same portion of memory to be acessed as different data types, since all of them are in fact the same location in memory.</p>
<p>union union_name {<br />
member_type1  member_name1;<br />
member_type2 member_name2;<br />
member_type3 member_name3;<br />
member_type4 member_name4;<br />
} object_names;</p>
<p>All the elemenst of the union declaration occupy the same physical space in memory. Its size is the one or the greatest. We can not store different values them independent of each other.</p>
<p><strong>QVariant</strong>: the QVariant class acts like a union for the most common Qt Data types.</p>
<p>C++ forbids unions from including types that have non-defaults constructor or destructor.</p>
<p>A QVariant objects holds a single value of a single type at time.</p>
<p><strong>QMetatype</strong>: It associates a type name to a type, so that it can be created and destructed dynamically at runtime.</p>
<p>Declare Q_DECLARE_METATYPE(type) to make them avaliable to QVariant.</p>
<p><strong>QString</strong>, <strong> QByteArray</strong> and <strong>QVariant</strong> are three classes that have many things in common with containers and that can be used as alternatives to containers in some context. Also like the containers, these classes use implicit sharing as memory and speed optmization.</p>
<p>Fonts:<br />
<a href="http://doc.qt.nokia.com" target="_blank">doc.qt.nokia.com</a><br />
<a href="http://www.cplusplus.com" target="_blank">www.cplusplus.com</a><br />
…........................................................................................................................</p>,-
author: Camila
categories: Archives, KDE, poo, Programming
date: "2011-02-22T19:31:35Z"
 
published: true
status: publish
tags: cpp, kde, plugin, quanta
title: typedef, union, QVariant and QMetatype.


<p>Just some notes about typedef, union, QVariant e QMetatype:</p>
<p><strong>typedef</strong>: allow the definition of our own types based on other existing data types.</p>
<p>typedef existing_type new_type_name;</p>
<p>typedef does not create a new type. It only create synonyms of a existing type.</p>
<p><strong>union</strong>: allow one same portion of memory to be acessed as different data types, since all of them are in fact the same location in memory.</p>
<p>union union_name {<br />
member_type1  member_name1;<br />
member_type2 member_name2;<br />
member_type3 member_name3;<br />
member_type4 member_name4;<br />
} object_names;</p>
<p>All the elemenst of the union declaration occupy the same physical space in memory. Its size is the one or the greatest. We can not store different values them independent of each other.</p>
<p><strong>QVariant</strong>: the QVariant class acts like a union for the most common Qt Data types.</p>
<p>C++ forbids unions from including types that have non-defaults constructor or destructor.</p>
<p>A QVariant objects holds a single value of a single type at time.</p>
<p><strong>QMetatype</strong>: It associates a type name to a type, so that it can be created and destructed dynamically at runtime.</p>
<p>Declare Q_DECLARE_METATYPE(type) to make them avaliable to QVariant.</p>
<p><strong>QString</strong>, <strong> QByteArray</strong> and <strong>QVariant</strong> are three classes that have many things in common with containers and that can be used as alternatives to containers in some context. Also like the containers, these classes use implicit sharing as memory and speed optmization.</p>
<p>Fonts:<br />
<a href="http://doc.qt.nokia.com" target="_blank">doc.qt.nokia.com</a><br />
<a href="http://www.cplusplus.com" target="_blank">www.cplusplus.com</a><br />
…........................................................................................................................</p>
<p>With these notes I intend to finish some new features in my plugin for Quanta :)</p>,-
author: Camila
categories: Archives, KDE, poo, Programming
date: "2011-02-22T19:31:35Z"
 
published: true
status: publish
tags: cpp, kde, plugin, quanta
title: typedef, union, QVariant and QMetatype.


<p>Just some notes about typedef, union, QVariant e QMetatype:</p>
<p><strong>typedef</strong>: allow the definition of our own types based on other existing data types.</p>
<p>typedef existing_type new_type_name;</p>
<p>typedef does not create a new type. It only create synonyms of a existing type.</p>
<p><strong>union</strong>: allow one same portion of memory to be acessed as different data types, since all of them are in fact the same location in memory.</p>
<p>union union_name {<br />
member_type1  member_name1;<br />
member_type2 member_name2;<br />
member_type3 member_name3;<br />
member_type4 member_name4;<br />
} object_names;</p>
<p>All the elemenst of the union declaration occupy the same physical space in memory. Its size is the one or the greatest. We can not store different values them independent of each other.</p>
<p><strong>QVariant</strong>: the QVariant class acts like a union for the most common Qt Data types.</p>
<p>C++ forbids unions from including types that have non-defaults constructor or destructor.</p>
<p>A QVariant objects holds a single value of a single type at time.</p>
<p><strong>QMetatype</strong>: It associates a type name to a type, so that it can be created and destructed dynamically at runtime.</p>
<p>Declare Q_DECLARE_METATYPE(type) to make them avaliable to QVariant.</p>
<p><strong>QString</strong>, <strong> QByteArray</strong> and <strong>QVariant</strong> are three classes that have many things in common with containers and that can be used as alternatives to containers in some context. Also like the containers, these classes use implicit sharing as memory and speed optmization.</p>
<p>Fonts:<br />
<a href="http://doc.qt.nokia.com" target="_blank">doc.qt.nokia.com</a><br />
<a href="http://www.cplusplus.com" target="_blank">www.cplusplus.com</a><br />
…........................................................................................................................</p>
<p>With these notes I intend to finish some new features in my plugin for Quanta :)</p>,-
author: Camila
categories: Archives, KDE, poo, Programming
date: "2011-02-22T19:31:35Z"
 
published: true
status: publish
tags: cpp, kde, plugin, quanta
title: typedef, union, QVariant and QMetatype.


<p>Just some notes about typedef, union, QVariant e QMetatype:</p>
<p><strong>typedef</strong>: allow the definition of our own types based on other existing data types.</p>
<p>typedef existing_type new_type_name;</p>
<p>typedef does not create a new type. It only create synonyms of a existing type.</p>
<p><strong>union</strong>: allow one same portion of memory to be acessed as different data types, since all of them are in fact the same location in memory.</p>
<p>union union_name {<br />
member_type1  member_name1;<br />
member_type2 member_name2;<br />
member_type3 member_name3;<br />
member_type4 member_name4;<br />
} object_names;</p>
<p>All the elemenst of the union declaration occupy the same physical space in memory. Its size is the one or the greatest. We can not store different values them independent of each other.</p>
<p><strong>QVariant</strong>: the QVariant class acts like a union for the most common Qt Data types.</p>
<p>C++ forbids unions from including types that have non-defaults constructor or destructor.</p>
<p>A QVariant objects holds a single value of a single type at time.</p>
<p><strong>QMetatype</strong>: It associates a type name to a type, so that it can be created and destructed dynamically at runtime.</p>
<p>Declare Q_DECLARE_METATYPE(type) to make them avaliable to QVariant.</p>
<p><strong>QString</strong>, <strong> QByteArray</strong> and <strong>QVariant</strong> are three classes that have many things in common with containers and that can be used as alternatives to containers in some context. Also like the containers, these classes use implicit sharing as memory and speed optmization.</p>
<p>Fonts:<br />
<a href="http://doc.qt.nokia.com" target="_blank">doc.qt.nokia.com</a><br />
<a href="http://www.cplusplus.com" target="_blank">www.cplusplus.com</a><br />
…........................................................................................................................</p>,-
author: Camila
categories: Archives, KDE, poo, Programming
date: "2011-02-22T19:31:35Z"
 
published: true
status: publish
tags: cpp, kde, plugin, quanta
title: typedef, union, QVariant and QMetatype.


<p>Just some notes about typedef, union, QVariant e QMetatype:</p>
<p><strong>typedef</strong>: allow the definition of our own types based on other existing data types.</p>
<p>typedef existing_type new_type_name;</p>
<p>typedef does not create a new type. It only create synonyms of a existing type.</p>
<p><strong>union</strong>: allow one same portion of memory to be acessed as different data types, since all of them are in fact the same location in memory.</p>
<p>union union_name {<br />
member_type1  member_name1;<br />
member_type2 member_name2;<br />
member_type3 member_name3;<br />
member_type4 member_name4;<br />
} object_names;</p>
<p>All the elemenst of the union declaration occupy the same physical space in memory. Its size is the one or the greatest. We can not store different values them independent of each other.</p>
<p><strong>QVariant</strong>: the QVariant class acts like a union for the most common Qt Data types.</p>
<p>C++ forbids unions from including types that have non-defaults constructor or destructor.</p>
<p>A QVariant objects holds a single value of a single type at time.</p>
<p><strong>QMetatype</strong>: It associates a type name to a type, so that it can be created and destructed dynamically at runtime.</p>
<p>Declare Q_DECLARE_METATYPE(type) to make them avaliable to QVariant.</p>
<p><strong>QString</strong>, <strong> QByteArray</strong> and <strong>QVariant</strong> are three classes that have many things in common with containers and that can be used as alternatives to containers in some context. Also like the containers, these classes use implicit sharing as memory and speed optmization.</p>
<p>Fonts:<br />
<a href="http://doc.qt.nokia.com" target="_blank">doc.qt.nokia.com</a><br />
<a href="http://www.cplusplus.com" target="_blank">www.cplusplus.com</a><br />
…........................................................................................................................</p>
<p>With these notes I intend to finish some new features in my plugin for Quanta :)</p>,-
author: Camila
categories: Archives, KDE, poo, Programming
date: "2011-02-22T19:31:35Z"
 
published: true
status: publish
tags: cpp, kde, plugin, quanta
title: typedef, union, QVariant and QMetatype.


<p>Just some notes about typedef, union, QVariant e QMetatype:</p>
<p><strong>typedef</strong>: allow the definition of our own types based on other existing data types.</p>
<p>typedef existing_type new_type_name;</p>
<p>typedef does not create a new type. It only create synonyms of a existing type.</p>
<p><strong>union</strong>: allow one same portion of memory to be acessed as different data types, since all of them are in fact the same location in memory.</p>
<p>union union_name {<br />
member_type1  member_name1;<br />
member_type2 member_name2;<br />
member_type3 member_name3;<br />
member_type4 member_name4;<br />
} object_names;</p>
<p>All the elemenst of the union declaration occupy the same physical space in memory. Its size is the one or the greatest. We can not store different values them independent of each other.</p>
<p><strong>QVariant</strong>: the QVariant class acts like a union for the most common Qt Data types.</p>
<p>C++ forbids unions from including types that have non-defaults constructor or destructor.</p>
<p>A QVariant objects holds a single value of a single type at time.</p>
<p><strong>QMetatype</strong>: It associates a type name to a type, so that it can be created and destructed dynamically at runtime.</p>
<p>Declare Q_DECLARE_METATYPE(type) to make them avaliable to QVariant.</p>
<p><strong>QString</strong>, <strong> QByteArray</strong> and <strong>QVariant</strong> are three classes that have many things in common with containers and that can be used as alternatives to containers in some context. Also like the containers, these classes use implicit sharing as memory and speed optmization.</p>
<p>Fonts:<br />
<a href="http://doc.qt.nokia.com" target="_blank">doc.qt.nokia.com</a><br />
<a href="http://www.cplusplus.com" target="_blank">www.cplusplus.com</a><br />
…........................................................................................................................</p>
<p>With these notes I intend to finish some new features in my plugin for Quanta :)</p>
