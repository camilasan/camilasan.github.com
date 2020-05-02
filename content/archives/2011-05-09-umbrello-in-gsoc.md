
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-05-09T07:53:18Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Umbrello in GSoC


<h1>My first week of work according to plan:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (I talked a bit with some class mates of GSoC)<br />
* Review Plan with Mentor. (I talked to Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>... and get used to work from home :)</p>
<h2>Porting Umbrello:</h2>
<p>I discovered that the best way to work would be to keep the old classes with the newly written ones together. Including calls for new methods in the same project so I can test the functionality of the new methods. Always comparing the new ones with the old ones.</p>
<p>The current result is Umbrello working with a new window showing the "new canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>In this "view" with QGraphicsView I can test my new classes.</p>
<h2>Using Squish to write tests:</h2>
<p>To try to make the best decision regarding how to proceed to the port, which parts of code reuse, I did a few class diagrams (just a draft), with the main classes that I should work with, I thought it would be interesting to draw the diagram in Umbrello, and save some steps using Squish</p>
<p>I'm using the Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - available only to test KDE software - you can ask one by e-mail: squishkde@froglogic.com. The advantage was to get some practice with the Software (I also discovered and reported some bugs :/)</p>
<p>It is very easy to write tests with Squish, you can automate the tests or write scripts by hand. What is tiring is that when you record the tests, the system stores a table with the objects of your application. But if the the object is not in this table, the test stops and you must include the object or editing the table by hand, or run the application in Spy mode or simply write "test dummies".</p>
<p>Read more here: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Some interesting links:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Next weeks:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>You can see my complete workplan here: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-05-09T07:53:18Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Umbrello in GSoC


<h1>My first week of work according to plan:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (I talked a bit with some class mates of GSoC)<br />
* Review Plan with Mentor. (I talked to Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>... and get used to work from home :)</p>
<h2>Porting Umbrello:</h2>
<p>I discovered that the best way to work would be to keep the old classes with the newly written ones together. Including calls for new methods in the same project so I can test the functionality of the new methods. Always comparing the new ones with the old ones.</p>
<p>The current result is Umbrello working with a new window showing the "new canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>In this "view" with QGraphicsView I can test my new classes.</p>
<h2>Using Squish to write tests:</h2>
<p>To try to make the best decision regarding how to proceed to the port, which parts of code reuse, I did a few class diagrams (just a draft), with the main classes that I should work with, I thought it would be interesting to draw the diagram in Umbrello, and save some steps using Squish</p>
<p>I'm using the Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - available only to test KDE software - you can ask one by e-mail: squishkde@froglogic.com. The advantage was to get some practice with the Software (I also discovered and reported some bugs :/)</p>
<p>It is very easy to write tests with Squish, you can automate the tests or write scripts by hand. What is tiring is that when you record the tests, the system stores a table with the objects of your application. But if the the object is not in this table, the test stops and you must include the object or editing the table by hand, or run the application in Spy mode or simply write "test dummies".</p>
<p>Read more here: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Some interesting links:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Next weeks:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>You can see my complete workplan here: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>
<p>I believe that like most students, my expectation with the GSoC is to LEARN a lot and perform a GOOD job. And even after that period CONTINUE contributing to the community:)</p>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-05-09T07:53:18Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Umbrello in GSoC


<h1>My first week of work according to plan:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (I talked a bit with some class mates of GSoC)<br />
* Review Plan with Mentor. (I talked to Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>... and get used to work from home :)</p>
<h2>Porting Umbrello:</h2>
<p>I discovered that the best way to work would be to keep the old classes with the newly written ones together. Including calls for new methods in the same project so I can test the functionality of the new methods. Always comparing the new ones with the old ones.</p>
<p>The current result is Umbrello working with a new window showing the "new canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>In this "view" with QGraphicsView I can test my new classes.</p>
<h2>Using Squish to write tests:</h2>
<p>To try to make the best decision regarding how to proceed to the port, which parts of code reuse, I did a few class diagrams (just a draft), with the main classes that I should work with, I thought it would be interesting to draw the diagram in Umbrello, and save some steps using Squish</p>
<p>I'm using the Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - available only to test KDE software - you can ask one by e-mail: squishkde@froglogic.com. The advantage was to get some practice with the Software (I also discovered and reported some bugs :/)</p>
<p>It is very easy to write tests with Squish, you can automate the tests or write scripts by hand. What is tiring is that when you record the tests, the system stores a table with the objects of your application. But if the the object is not in this table, the test stops and you must include the object or editing the table by hand, or run the application in Spy mode or simply write "test dummies".</p>
<p>Read more here: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Some interesting links:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Next weeks:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>You can see my complete workplan here: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-05-09T07:53:18Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Umbrello in GSoC


<h1>My first week of work according to plan:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (I talked a bit with some class mates of GSoC)<br />
* Review Plan with Mentor. (I talked to Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>... and get used to work from home :)</p>
<h2>Porting Umbrello:</h2>
<p>I discovered that the best way to work would be to keep the old classes with the newly written ones together. Including calls for new methods in the same project so I can test the functionality of the new methods. Always comparing the new ones with the old ones.</p>
<p>The current result is Umbrello working with a new window showing the "new canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>In this "view" with QGraphicsView I can test my new classes.</p>
<h2>Using Squish to write tests:</h2>
<p>To try to make the best decision regarding how to proceed to the port, which parts of code reuse, I did a few class diagrams (just a draft), with the main classes that I should work with, I thought it would be interesting to draw the diagram in Umbrello, and save some steps using Squish</p>
<p>I'm using the Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - available only to test KDE software - you can ask one by e-mail: squishkde@froglogic.com. The advantage was to get some practice with the Software (I also discovered and reported some bugs :/)</p>
<p>It is very easy to write tests with Squish, you can automate the tests or write scripts by hand. What is tiring is that when you record the tests, the system stores a table with the objects of your application. But if the the object is not in this table, the test stops and you must include the object or editing the table by hand, or run the application in Spy mode or simply write "test dummies".</p>
<p>Read more here: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Some interesting links:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Next weeks:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>You can see my complete workplan here: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-05-09T07:53:18Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Umbrello in GSoC


<h1>My first week of work according to plan:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (I talked a bit with some class mates of GSoC)<br />
* Review Plan with Mentor. (I talked to Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>... and get used to work from home :)</p>
<h2>Porting Umbrello:</h2>
<p>I discovered that the best way to work would be to keep the old classes with the newly written ones together. Including calls for new methods in the same project so I can test the functionality of the new methods. Always comparing the new ones with the old ones.</p>
<p>The current result is Umbrello working with a new window showing the "new canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>In this "view" with QGraphicsView I can test my new classes.</p>
<h2>Using Squish to write tests:</h2>
<p>To try to make the best decision regarding how to proceed to the port, which parts of code reuse, I did a few class diagrams (just a draft), with the main classes that I should work with, I thought it would be interesting to draw the diagram in Umbrello, and save some steps using Squish</p>
<p>I'm using the Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - available only to test KDE software - you can ask one by e-mail: squishkde@froglogic.com. The advantage was to get some practice with the Software (I also discovered and reported some bugs :/)</p>
<p>It is very easy to write tests with Squish, you can automate the tests or write scripts by hand. What is tiring is that when you record the tests, the system stores a table with the objects of your application. But if the the object is not in this table, the test stops and you must include the object or editing the table by hand, or run the application in Spy mode or simply write "test dummies".</p>
<p>Read more here: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Some interesting links:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Next weeks:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>You can see my complete workplan here: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>
<p>I believe that like most students, my expectation with the GSoC is to LEARN a lot and perform a GOOD job. And even after that period CONTINUE contributing to the community:)</p>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-05-09T07:53:18Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Umbrello in GSoC


<h1>My first week of work according to plan:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (I talked a bit with some class mates of GSoC)<br />
* Review Plan with Mentor. (I talked to Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>... and get used to work from home :)</p>
<h2>Porting Umbrello:</h2>
<p>I discovered that the best way to work would be to keep the old classes with the newly written ones together. Including calls for new methods in the same project so I can test the functionality of the new methods. Always comparing the new ones with the old ones.</p>
<p>The current result is Umbrello working with a new window showing the "new canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>In this "view" with QGraphicsView I can test my new classes.</p>
<h2>Using Squish to write tests:</h2>
<p>To try to make the best decision regarding how to proceed to the port, which parts of code reuse, I did a few class diagrams (just a draft), with the main classes that I should work with, I thought it would be interesting to draw the diagram in Umbrello, and save some steps using Squish</p>
<p>I'm using the Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - available only to test KDE software - you can ask one by e-mail: squishkde@froglogic.com. The advantage was to get some practice with the Software (I also discovered and reported some bugs :/)</p>
<p>It is very easy to write tests with Squish, you can automate the tests or write scripts by hand. What is tiring is that when you record the tests, the system stores a table with the objects of your application. But if the the object is not in this table, the test stops and you must include the object or editing the table by hand, or run the application in Spy mode or simply write "test dummies".</p>
<p>Read more here: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Some interesting links:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Next weeks:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>You can see my complete workplan here: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>
<p>I believe that like most students, my expectation with the GSoC is to LEARN a lot and perform a GOOD job. And even after that period CONTINUE contributing to the community:)</p>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-05-09T07:53:18Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Umbrello in GSoC


<h1>My first week of work according to plan:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (I talked a bit with some class mates of GSoC)<br />
* Review Plan with Mentor. (I talked to Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>... and get used to work from home :)</p>
<h2>Porting Umbrello:</h2>
<p>I discovered that the best way to work would be to keep the old classes with the newly written ones together. Including calls for new methods in the same project so I can test the functionality of the new methods. Always comparing the new ones with the old ones.</p>
<p>The current result is Umbrello working with a new window showing the "new canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>In this "view" with QGraphicsView I can test my new classes.</p>
<h2>Using Squish to write tests:</h2>
<p>To try to make the best decision regarding how to proceed to the port, which parts of code reuse, I did a few class diagrams (just a draft), with the main classes that I should work with, I thought it would be interesting to draw the diagram in Umbrello, and save some steps using Squish</p>
<p>I'm using the Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - available only to test KDE software - you can ask one by e-mail: squishkde@froglogic.com. The advantage was to get some practice with the Software (I also discovered and reported some bugs :/)</p>
<p>It is very easy to write tests with Squish, you can automate the tests or write scripts by hand. What is tiring is that when you record the tests, the system stores a table with the objects of your application. But if the the object is not in this table, the test stops and you must include the object or editing the table by hand, or run the application in Spy mode or simply write "test dummies".</p>
<p>Read more here: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Some interesting links:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Next weeks:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>You can see my complete workplan here: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-05-09T07:53:18Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Umbrello in GSoC


<h1>My first week of work according to plan:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (I talked a bit with some class mates of GSoC)<br />
* Review Plan with Mentor. (I talked to Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>... and get used to work from home :)</p>
<h2>Porting Umbrello:</h2>
<p>I discovered that the best way to work would be to keep the old classes with the newly written ones together. Including calls for new methods in the same project so I can test the functionality of the new methods. Always comparing the new ones with the old ones.</p>
<p>The current result is Umbrello working with a new window showing the "new canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>In this "view" with QGraphicsView I can test my new classes.</p>
<h2>Using Squish to write tests:</h2>
<p>To try to make the best decision regarding how to proceed to the port, which parts of code reuse, I did a few class diagrams (just a draft), with the main classes that I should work with, I thought it would be interesting to draw the diagram in Umbrello, and save some steps using Squish</p>
<p>I'm using the Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - available only to test KDE software - you can ask one by e-mail: squishkde@froglogic.com. The advantage was to get some practice with the Software (I also discovered and reported some bugs :/)</p>
<p>It is very easy to write tests with Squish, you can automate the tests or write scripts by hand. What is tiring is that when you record the tests, the system stores a table with the objects of your application. But if the the object is not in this table, the test stops and you must include the object or editing the table by hand, or run the application in Spy mode or simply write "test dummies".</p>
<p>Read more here: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Some interesting links:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Next weeks:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>You can see my complete workplan here: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>
<p>I believe that like most students, my expectation with the GSoC is to LEARN a lot and perform a GOOD job. And even after that period CONTINUE contributing to the community:)</p>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-05-09T07:53:18Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Umbrello in GSoC


<h1>My first week of work according to plan:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (I talked a bit with some class mates of GSoC)<br />
* Review Plan with Mentor. (I talked to Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>... and get used to work from home :)</p>
<h2>Porting Umbrello:</h2>
<p>I discovered that the best way to work would be to keep the old classes with the newly written ones together. Including calls for new methods in the same project so I can test the functionality of the new methods. Always comparing the new ones with the old ones.</p>
<p>The current result is Umbrello working with a new window showing the "new canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>In this "view" with QGraphicsView I can test my new classes.</p>
<h2>Using Squish to write tests:</h2>
<p>To try to make the best decision regarding how to proceed to the port, which parts of code reuse, I did a few class diagrams (just a draft), with the main classes that I should work with, I thought it would be interesting to draw the diagram in Umbrello, and save some steps using Squish</p>
<p>I'm using the Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - available only to test KDE software - you can ask one by e-mail: squishkde@froglogic.com. The advantage was to get some practice with the Software (I also discovered and reported some bugs :/)</p>
<p>It is very easy to write tests with Squish, you can automate the tests or write scripts by hand. What is tiring is that when you record the tests, the system stores a table with the objects of your application. But if the the object is not in this table, the test stops and you must include the object or editing the table by hand, or run the application in Spy mode or simply write "test dummies".</p>
<p>Read more here: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Some interesting links:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Next weeks:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>You can see my complete workplan here: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>
<p>I believe that like most students, my expectation with the GSoC is to LEARN a lot and perform a GOOD job. And even after that period CONTINUE contributing to the community:)</p>
