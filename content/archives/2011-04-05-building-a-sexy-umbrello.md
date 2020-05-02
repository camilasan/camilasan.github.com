
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-04-05T23:36:45Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Building a sexy Umbrello


<p>I'm  a big fan of <a title="Umbrello" href="http://uml.sourceforge.net/" target="_blank">Umbrello</a>. It's a Free Software graphical <a title="UML" href="http://www.uml.org" target="_blank">UML</a> (Unified   Modeling Language) editor, one of the very few of it's kind. Most <a title="UML Tools" href="http://en.wikipedia.org/wiki/List_of_Unified_Modeling_Language_tools" target="_blank">UML tools are proprietary tools written in Java</a> and Umbrello is written in  C++/Qt and build on the powerful base of KDE  software. I realized how  interesting Umbrello is when I noticed that the  most of my professors  suggest proprietary tools or a <a href="http://projects.gnome.org/dia/" target="_blank">generic diagramming program with few UML features</a> to study UML at college class. Many companies use UML to help them quickly write applications and Umbrello is (as far as I know) the only Free Software tool which can do the code generation required for that!</p>
<h2>Why UML is important?</h2>
<p>"<em>Modeling  is the designing of software applications before coding. Modeling is an  Essential Part of large software projects, and helpful to medium and  even small projects as well. (...) Using a model, those responsible for a  software development project's success can assure themselves that  business functionality is complete and correct, end-user needs are met,  and program design supports requirements for scalability(...)</em>"<br />
<a href="http://www.omg.org/gettingstarted/what_is_uml.htm">http://www.omg.org/gettingstarted/what_is_uml.htm</a></p>
<p>Of course, It is not only my college that uses UML, there are a lot of company wich use UML tools in their development process, including  companies where I have worked and you can find some more examples <a href="http://www.uml.org/uml_success_stories/index.htm" target="_blank">here</a>.</p>
<h2>Umbrello</h2>
<p>So having a Free Software UML editor is pretty important! And the Umbrello UML editor is really cool:</p>
<ul>
<li>
Automatic code generation (Ada, C++, C#, Java, perl, PHP, Python, Ruby)</li>
<li>Import classes and project (Ada, C++, IDL, Java, Pascal and Python only)</li>
</ul>
<p>The  bad news is that Umbrello does not receive a lot of love. It has been  roughly ported to Qt4 and KDElibs4 but still uses a lot of Q3Canvas classes and has quite a few bugs.</p>
<p>[caption id="attachment_408" align="aligncenter" width="630" caption="Umbrello"]<a href="http://uml.sourceforge.net/"><img class="size-full wp-image-408 " title="Umbrello" src="/assets/images/diagram.png" alt="Umbrello today" width="630" height="369" /></a>[/caption]</p>
<h2>Working on Umbrello</h2>
<p>Which  is why I choose Umbrello for my conclusion work for the University. I  would have to work on something anyway, why not pick something that  matters? But as I combine my study (5 nights with each a different  class) with a full-time job I don't have a lot of  time to do a proper job on Umbrello. My goal for the University is  therefore pretty modest: I intend to finish the port of the canvas to  QGraphicsView. I have identified about 30 classes which are related to the Q3Canvas and will have to be ported or replaced. I also intend to use tools for automated tests, write unit tests and and fix some bugs.</p>
<div>But there is more to do:</div>
<ul>
<li>Better stereotypes supports</li>
<li>Complete Undo/Redo  support</li>
<li>Hyperlinks support</li>
<li>Reuse KDevelop analysis for code import
</li>
<li>Bug fixing</li>
</ul>
<h2>GSoC 2011</h2>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-04-05T23:36:45Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Building a sexy Umbrello


<p>I'm  a big fan of <a title="Umbrello" href="http://uml.sourceforge.net/" target="_blank">Umbrello</a>. It's a Free Software graphical <a title="UML" href="http://www.uml.org" target="_blank">UML</a> (Unified   Modeling Language) editor, one of the very few of it's kind. Most <a title="UML Tools" href="http://en.wikipedia.org/wiki/List_of_Unified_Modeling_Language_tools" target="_blank">UML tools are proprietary tools written in Java</a> and Umbrello is written in  C++/Qt and build on the powerful base of KDE  software. I realized how  interesting Umbrello is when I noticed that the  most of my professors  suggest proprietary tools or a <a href="http://projects.gnome.org/dia/" target="_blank">generic diagramming program with few UML features</a> to study UML at college class. Many companies use UML to help them quickly write applications and Umbrello is (as far as I know) the only Free Software tool which can do the code generation required for that!</p>
<h2>Why UML is important?</h2>
<p>"<em>Modeling  is the designing of software applications before coding. Modeling is an  Essential Part of large software projects, and helpful to medium and  even small projects as well. (...) Using a model, those responsible for a  software development project's success can assure themselves that  business functionality is complete and correct, end-user needs are met,  and program design supports requirements for scalability(...)</em>"<br />
<a href="http://www.omg.org/gettingstarted/what_is_uml.htm">http://www.omg.org/gettingstarted/what_is_uml.htm</a></p>
<p>Of course, It is not only my college that uses UML, there are a lot of company wich use UML tools in their development process, including  companies where I have worked and you can find some more examples <a href="http://www.uml.org/uml_success_stories/index.htm" target="_blank">here</a>.</p>
<h2>Umbrello</h2>
<p>So having a Free Software UML editor is pretty important! And the Umbrello UML editor is really cool:</p>
<ul>
<li>
Automatic code generation (Ada, C++, C#, Java, perl, PHP, Python, Ruby)</li>
<li>Import classes and project (Ada, C++, IDL, Java, Pascal and Python only)</li>
</ul>
<p>The  bad news is that Umbrello does not receive a lot of love. It has been  roughly ported to Qt4 and KDElibs4 but still uses a lot of Q3Canvas classes and has quite a few bugs.</p>
<p>[caption id="attachment_408" align="aligncenter" width="630" caption="Umbrello"]<a href="http://uml.sourceforge.net/"><img class="size-full wp-image-408 " title="Umbrello" src="/assets/images/diagram.png" alt="Umbrello today" width="630" height="369" /></a>[/caption]</p>
<h2>Working on Umbrello</h2>
<p>Which  is why I choose Umbrello for my conclusion work for the University. I  would have to work on something anyway, why not pick something that  matters? But as I combine my study (5 nights with each a different  class) with a full-time job I don't have a lot of  time to do a proper job on Umbrello. My goal for the University is  therefore pretty modest: I intend to finish the port of the canvas to  QGraphicsView. I have identified about 30 classes which are related to the Q3Canvas and will have to be ported or replaced. I also intend to use tools for automated tests, write unit tests and and fix some bugs.</p>
<div>But there is more to do:</div>
<ul>
<li>Better stereotypes supports</li>
<li>Complete Undo/Redo  support</li>
<li>Hyperlinks support</li>
<li>Reuse KDevelop analysis for code import
</li>
<li>Bug fixing</li>
</ul>
<h2>GSoC 2011</h2>
<p>So  I have applied for a Google Summer of Code. Jonathan Riddel, the  current maintainer of Umbrello, has said he would mentor me, which is  really cool. So if I get this, I can quit my current job and finish the  porting to QGraphicsView much faster. To ensure it'll be a successful  project, I've been quite modest in my goals for GSoC too: I only  shortened my university plan to the GSoC timeline and added a few small  things. If I finish the work for my conclusion work during the GSoC, I can be  more ambitious for my University and add to the plan - I'm sure my  professor won't mind if I take on some feature work in Umbrello as well!</p>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-04-05T23:36:45Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Building a sexy Umbrello


<p>I'm  a big fan of <a title="Umbrello" href="http://uml.sourceforge.net/" target="_blank">Umbrello</a>. It's a Free Software graphical <a title="UML" href="http://www.uml.org" target="_blank">UML</a> (Unified   Modeling Language) editor, one of the very few of it's kind. Most <a title="UML Tools" href="http://en.wikipedia.org/wiki/List_of_Unified_Modeling_Language_tools" target="_blank">UML tools are proprietary tools written in Java</a> and Umbrello is written in  C++/Qt and build on the powerful base of KDE  software. I realized how  interesting Umbrello is when I noticed that the  most of my professors  suggest proprietary tools or a <a href="http://projects.gnome.org/dia/" target="_blank">generic diagramming program with few UML features</a> to study UML at college class. Many companies use UML to help them quickly write applications and Umbrello is (as far as I know) the only Free Software tool which can do the code generation required for that!</p>
<h2>Why UML is important?</h2>
<p>"<em>Modeling  is the designing of software applications before coding. Modeling is an  Essential Part of large software projects, and helpful to medium and  even small projects as well. (...) Using a model, those responsible for a  software development project's success can assure themselves that  business functionality is complete and correct, end-user needs are met,  and program design supports requirements for scalability(...)</em>"<br />
<a href="http://www.omg.org/gettingstarted/what_is_uml.htm">http://www.omg.org/gettingstarted/what_is_uml.htm</a></p>
<p>Of course, It is not only my college that uses UML, there are a lot of company wich use UML tools in their development process, including  companies where I have worked and you can find some more examples <a href="http://www.uml.org/uml_success_stories/index.htm" target="_blank">here</a>.</p>
<h2>Umbrello</h2>
<p>So having a Free Software UML editor is pretty important! And the Umbrello UML editor is really cool:</p>
<ul>
<li>
Automatic code generation (Ada, C++, C#, Java, perl, PHP, Python, Ruby)</li>
<li>Import classes and project (Ada, C++, IDL, Java, Pascal and Python only)</li>
</ul>
<p>The  bad news is that Umbrello does not receive a lot of love. It has been  roughly ported to Qt4 and KDElibs4 but still uses a lot of Q3Canvas classes and has quite a few bugs.</p>
<p>[caption id="attachment_408" align="aligncenter" width="630" caption="Umbrello"]<a href="http://uml.sourceforge.net/"><img class="size-full wp-image-408 " title="Umbrello" src="/assets/images/diagram.png" alt="Umbrello today" width="630" height="369" /></a>[/caption]</p>
<h2>Working on Umbrello</h2>
<p>Which  is why I choose Umbrello for my conclusion work for the University. I  would have to work on something anyway, why not pick something that  matters? But as I combine my study (5 nights with each a different  class) with a full-time job I don't have a lot of  time to do a proper job on Umbrello. My goal for the University is  therefore pretty modest: I intend to finish the port of the canvas to  QGraphicsView. I have identified about 30 classes which are related to the Q3Canvas and will have to be ported or replaced. I also intend to use tools for automated tests, write unit tests and and fix some bugs.</p>
<div>But there is more to do:</div>
<ul>
<li>Better stereotypes supports</li>
<li>Complete Undo/Redo  support</li>
<li>Hyperlinks support</li>
<li>Reuse KDevelop analysis for code import
</li>
<li>Bug fixing</li>
</ul>
<h2>GSoC 2011</h2>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-04-05T23:36:45Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Building a sexy Umbrello


<p>I'm  a big fan of <a title="Umbrello" href="http://uml.sourceforge.net/" target="_blank">Umbrello</a>. It's a Free Software graphical <a title="UML" href="http://www.uml.org" target="_blank">UML</a> (Unified   Modeling Language) editor, one of the very few of it's kind. Most <a title="UML Tools" href="http://en.wikipedia.org/wiki/List_of_Unified_Modeling_Language_tools" target="_blank">UML tools are proprietary tools written in Java</a> and Umbrello is written in  C++/Qt and build on the powerful base of KDE  software. I realized how  interesting Umbrello is when I noticed that the  most of my professors  suggest proprietary tools or a <a href="http://projects.gnome.org/dia/" target="_blank">generic diagramming program with few UML features</a> to study UML at college class. Many companies use UML to help them quickly write applications and Umbrello is (as far as I know) the only Free Software tool which can do the code generation required for that!</p>
<h2>Why UML is important?</h2>
<p>"<em>Modeling  is the designing of software applications before coding. Modeling is an  Essential Part of large software projects, and helpful to medium and  even small projects as well. (...) Using a model, those responsible for a  software development project's success can assure themselves that  business functionality is complete and correct, end-user needs are met,  and program design supports requirements for scalability(...)</em>"<br />
<a href="http://www.omg.org/gettingstarted/what_is_uml.htm">http://www.omg.org/gettingstarted/what_is_uml.htm</a></p>
<p>Of course, It is not only my college that uses UML, there are a lot of company wich use UML tools in their development process, including  companies where I have worked and you can find some more examples <a href="http://www.uml.org/uml_success_stories/index.htm" target="_blank">here</a>.</p>
<h2>Umbrello</h2>
<p>So having a Free Software UML editor is pretty important! And the Umbrello UML editor is really cool:</p>
<ul>
<li>
Automatic code generation (Ada, C++, C#, Java, perl, PHP, Python, Ruby)</li>
<li>Import classes and project (Ada, C++, IDL, Java, Pascal and Python only)</li>
</ul>
<p>The  bad news is that Umbrello does not receive a lot of love. It has been  roughly ported to Qt4 and KDElibs4 but still uses a lot of Q3Canvas classes and has quite a few bugs.</p>
<p>[caption id="attachment_408" align="aligncenter" width="630" caption="Umbrello"]<a href="http://uml.sourceforge.net/"><img class="size-full wp-image-408 " title="Umbrello" src="/assets/images/diagram.png" alt="Umbrello today" width="630" height="369" /></a>[/caption]</p>
<h2>Working on Umbrello</h2>
<p>Which  is why I choose Umbrello for my conclusion work for the University. I  would have to work on something anyway, why not pick something that  matters? But as I combine my study (5 nights with each a different  class) with a full-time job I don't have a lot of  time to do a proper job on Umbrello. My goal for the University is  therefore pretty modest: I intend to finish the port of the canvas to  QGraphicsView. I have identified about 30 classes which are related to the Q3Canvas and will have to be ported or replaced. I also intend to use tools for automated tests, write unit tests and and fix some bugs.</p>
<div>But there is more to do:</div>
<ul>
<li>Better stereotypes supports</li>
<li>Complete Undo/Redo  support</li>
<li>Hyperlinks support</li>
<li>Reuse KDevelop analysis for code import
</li>
<li>Bug fixing</li>
</ul>
<h2>GSoC 2011</h2>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-04-05T23:36:45Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Building a sexy Umbrello


<p>I'm  a big fan of <a title="Umbrello" href="http://uml.sourceforge.net/" target="_blank">Umbrello</a>. It's a Free Software graphical <a title="UML" href="http://www.uml.org" target="_blank">UML</a> (Unified   Modeling Language) editor, one of the very few of it's kind. Most <a title="UML Tools" href="http://en.wikipedia.org/wiki/List_of_Unified_Modeling_Language_tools" target="_blank">UML tools are proprietary tools written in Java</a> and Umbrello is written in  C++/Qt and build on the powerful base of KDE  software. I realized how  interesting Umbrello is when I noticed that the  most of my professors  suggest proprietary tools or a <a href="http://projects.gnome.org/dia/" target="_blank">generic diagramming program with few UML features</a> to study UML at college class. Many companies use UML to help them quickly write applications and Umbrello is (as far as I know) the only Free Software tool which can do the code generation required for that!</p>
<h2>Why UML is important?</h2>
<p>"<em>Modeling  is the designing of software applications before coding. Modeling is an  Essential Part of large software projects, and helpful to medium and  even small projects as well. (...) Using a model, those responsible for a  software development project's success can assure themselves that  business functionality is complete and correct, end-user needs are met,  and program design supports requirements for scalability(...)</em>"<br />
<a href="http://www.omg.org/gettingstarted/what_is_uml.htm">http://www.omg.org/gettingstarted/what_is_uml.htm</a></p>
<p>Of course, It is not only my college that uses UML, there are a lot of company wich use UML tools in their development process, including  companies where I have worked and you can find some more examples <a href="http://www.uml.org/uml_success_stories/index.htm" target="_blank">here</a>.</p>
<h2>Umbrello</h2>
<p>So having a Free Software UML editor is pretty important! And the Umbrello UML editor is really cool:</p>
<ul>
<li>
Automatic code generation (Ada, C++, C#, Java, perl, PHP, Python, Ruby)</li>
<li>Import classes and project (Ada, C++, IDL, Java, Pascal and Python only)</li>
</ul>
<p>The  bad news is that Umbrello does not receive a lot of love. It has been  roughly ported to Qt4 and KDElibs4 but still uses a lot of Q3Canvas classes and has quite a few bugs.</p>
<p>[caption id="attachment_408" align="aligncenter" width="630" caption="Umbrello"]<a href="http://uml.sourceforge.net/"><img class="size-full wp-image-408 " title="Umbrello" src="/assets/images/diagram.png" alt="Umbrello today" width="630" height="369" /></a>[/caption]</p>
<h2>Working on Umbrello</h2>
<p>Which  is why I choose Umbrello for my conclusion work for the University. I  would have to work on something anyway, why not pick something that  matters? But as I combine my study (5 nights with each a different  class) with a full-time job I don't have a lot of  time to do a proper job on Umbrello. My goal for the University is  therefore pretty modest: I intend to finish the port of the canvas to  QGraphicsView. I have identified about 30 classes which are related to the Q3Canvas and will have to be ported or replaced. I also intend to use tools for automated tests, write unit tests and and fix some bugs.</p>
<div>But there is more to do:</div>
<ul>
<li>Better stereotypes supports</li>
<li>Complete Undo/Redo  support</li>
<li>Hyperlinks support</li>
<li>Reuse KDevelop analysis for code import
</li>
<li>Bug fixing</li>
</ul>
<h2>GSoC 2011</h2>
<p>So  I have applied for a Google Summer of Code. Jonathan Riddel, the  current maintainer of Umbrello, has said he would mentor me, which is  really cool. So if I get this, I can quit my current job and finish the  porting to QGraphicsView much faster. To ensure it'll be a successful  project, I've been quite modest in my goals for GSoC too: I only  shortened my university plan to the GSoC timeline and added a few small  things. If I finish the work for my conclusion work during the GSoC, I can be  more ambitious for my University and add to the plan - I'm sure my  professor won't mind if I take on some feature work in Umbrello as well!</p>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-04-05T23:36:45Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Building a sexy Umbrello


<p>I'm  a big fan of <a title="Umbrello" href="http://uml.sourceforge.net/" target="_blank">Umbrello</a>. It's a Free Software graphical <a title="UML" href="http://www.uml.org" target="_blank">UML</a> (Unified   Modeling Language) editor, one of the very few of it's kind. Most <a title="UML Tools" href="http://en.wikipedia.org/wiki/List_of_Unified_Modeling_Language_tools" target="_blank">UML tools are proprietary tools written in Java</a> and Umbrello is written in  C++/Qt and build on the powerful base of KDE  software. I realized how  interesting Umbrello is when I noticed that the  most of my professors  suggest proprietary tools or a <a href="http://projects.gnome.org/dia/" target="_blank">generic diagramming program with few UML features</a> to study UML at college class. Many companies use UML to help them quickly write applications and Umbrello is (as far as I know) the only Free Software tool which can do the code generation required for that!</p>
<h2>Why UML is important?</h2>
<p>"<em>Modeling  is the designing of software applications before coding. Modeling is an  Essential Part of large software projects, and helpful to medium and  even small projects as well. (...) Using a model, those responsible for a  software development project's success can assure themselves that  business functionality is complete and correct, end-user needs are met,  and program design supports requirements for scalability(...)</em>"<br />
<a href="http://www.omg.org/gettingstarted/what_is_uml.htm">http://www.omg.org/gettingstarted/what_is_uml.htm</a></p>
<p>Of course, It is not only my college that uses UML, there are a lot of company wich use UML tools in their development process, including  companies where I have worked and you can find some more examples <a href="http://www.uml.org/uml_success_stories/index.htm" target="_blank">here</a>.</p>
<h2>Umbrello</h2>
<p>So having a Free Software UML editor is pretty important! And the Umbrello UML editor is really cool:</p>
<ul>
<li>
Automatic code generation (Ada, C++, C#, Java, perl, PHP, Python, Ruby)</li>
<li>Import classes and project (Ada, C++, IDL, Java, Pascal and Python only)</li>
</ul>
<p>The  bad news is that Umbrello does not receive a lot of love. It has been  roughly ported to Qt4 and KDElibs4 but still uses a lot of Q3Canvas classes and has quite a few bugs.</p>
<p>[caption id="attachment_408" align="aligncenter" width="630" caption="Umbrello"]<a href="http://uml.sourceforge.net/"><img class="size-full wp-image-408 " title="Umbrello" src="/assets/images/diagram.png" alt="Umbrello today" width="630" height="369" /></a>[/caption]</p>
<h2>Working on Umbrello</h2>
<p>Which  is why I choose Umbrello for my conclusion work for the University. I  would have to work on something anyway, why not pick something that  matters? But as I combine my study (5 nights with each a different  class) with a full-time job I don't have a lot of  time to do a proper job on Umbrello. My goal for the University is  therefore pretty modest: I intend to finish the port of the canvas to  QGraphicsView. I have identified about 30 classes which are related to the Q3Canvas and will have to be ported or replaced. I also intend to use tools for automated tests, write unit tests and and fix some bugs.</p>
<div>But there is more to do:</div>
<ul>
<li>Better stereotypes supports</li>
<li>Complete Undo/Redo  support</li>
<li>Hyperlinks support</li>
<li>Reuse KDevelop analysis for code import
</li>
<li>Bug fixing</li>
</ul>
<h2>GSoC 2011</h2>
<p>So  I have applied for a Google Summer of Code. Jonathan Riddel, the  current maintainer of Umbrello, has said he would mentor me, which is  really cool. So if I get this, I can quit my current job and finish the  porting to QGraphicsView much faster. To ensure it'll be a successful  project, I've been quite modest in my goals for GSoC too: I only  shortened my university plan to the GSoC timeline and added a few small  things. If I finish the work for my conclusion work during the GSoC, I can be  more ambitious for my University and add to the plan - I'm sure my  professor won't mind if I take on some feature work in Umbrello as well!</p>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-04-05T23:36:45Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Building a sexy Umbrello


<p>I'm  a big fan of <a title="Umbrello" href="http://uml.sourceforge.net/" target="_blank">Umbrello</a>. It's a Free Software graphical <a title="UML" href="http://www.uml.org" target="_blank">UML</a> (Unified   Modeling Language) editor, one of the very few of it's kind. Most <a title="UML Tools" href="http://en.wikipedia.org/wiki/List_of_Unified_Modeling_Language_tools" target="_blank">UML tools are proprietary tools written in Java</a> and Umbrello is written in  C++/Qt and build on the powerful base of KDE  software. I realized how  interesting Umbrello is when I noticed that the  most of my professors  suggest proprietary tools or a <a href="http://projects.gnome.org/dia/" target="_blank">generic diagramming program with few UML features</a> to study UML at college class. Many companies use UML to help them quickly write applications and Umbrello is (as far as I know) the only Free Software tool which can do the code generation required for that!</p>
<h2>Why UML is important?</h2>
<p>"<em>Modeling  is the designing of software applications before coding. Modeling is an  Essential Part of large software projects, and helpful to medium and  even small projects as well. (...) Using a model, those responsible for a  software development project's success can assure themselves that  business functionality is complete and correct, end-user needs are met,  and program design supports requirements for scalability(...)</em>"<br />
<a href="http://www.omg.org/gettingstarted/what_is_uml.htm">http://www.omg.org/gettingstarted/what_is_uml.htm</a></p>
<p>Of course, It is not only my college that uses UML, there are a lot of company wich use UML tools in their development process, including  companies where I have worked and you can find some more examples <a href="http://www.uml.org/uml_success_stories/index.htm" target="_blank">here</a>.</p>
<h2>Umbrello</h2>
<p>So having a Free Software UML editor is pretty important! And the Umbrello UML editor is really cool:</p>
<ul>
<li>
Automatic code generation (Ada, C++, C#, Java, perl, PHP, Python, Ruby)</li>
<li>Import classes and project (Ada, C++, IDL, Java, Pascal and Python only)</li>
</ul>
<p>The  bad news is that Umbrello does not receive a lot of love. It has been  roughly ported to Qt4 and KDElibs4 but still uses a lot of Q3Canvas classes and has quite a few bugs.</p>
<p>[caption id="attachment_408" align="aligncenter" width="630" caption="Umbrello"]<a href="http://uml.sourceforge.net/"><img class="size-full wp-image-408 " title="Umbrello" src="/assets/images/diagram.png" alt="Umbrello today" width="630" height="369" /></a>[/caption]</p>
<h2>Working on Umbrello</h2>
<p>Which  is why I choose Umbrello for my conclusion work for the University. I  would have to work on something anyway, why not pick something that  matters? But as I combine my study (5 nights with each a different  class) with a full-time job I don't have a lot of  time to do a proper job on Umbrello. My goal for the University is  therefore pretty modest: I intend to finish the port of the canvas to  QGraphicsView. I have identified about 30 classes which are related to the Q3Canvas and will have to be ported or replaced. I also intend to use tools for automated tests, write unit tests and and fix some bugs.</p>
<div>But there is more to do:</div>
<ul>
<li>Better stereotypes supports</li>
<li>Complete Undo/Redo  support</li>
<li>Hyperlinks support</li>
<li>Reuse KDevelop analysis for code import
</li>
<li>Bug fixing</li>
</ul>
<h2>GSoC 2011</h2>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-04-05T23:36:45Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Building a sexy Umbrello


<p>I'm  a big fan of <a title="Umbrello" href="http://uml.sourceforge.net/" target="_blank">Umbrello</a>. It's a Free Software graphical <a title="UML" href="http://www.uml.org" target="_blank">UML</a> (Unified   Modeling Language) editor, one of the very few of it's kind. Most <a title="UML Tools" href="http://en.wikipedia.org/wiki/List_of_Unified_Modeling_Language_tools" target="_blank">UML tools are proprietary tools written in Java</a> and Umbrello is written in  C++/Qt and build on the powerful base of KDE  software. I realized how  interesting Umbrello is when I noticed that the  most of my professors  suggest proprietary tools or a <a href="http://projects.gnome.org/dia/" target="_blank">generic diagramming program with few UML features</a> to study UML at college class. Many companies use UML to help them quickly write applications and Umbrello is (as far as I know) the only Free Software tool which can do the code generation required for that!</p>
<h2>Why UML is important?</h2>
<p>"<em>Modeling  is the designing of software applications before coding. Modeling is an  Essential Part of large software projects, and helpful to medium and  even small projects as well. (...) Using a model, those responsible for a  software development project's success can assure themselves that  business functionality is complete and correct, end-user needs are met,  and program design supports requirements for scalability(...)</em>"<br />
<a href="http://www.omg.org/gettingstarted/what_is_uml.htm">http://www.omg.org/gettingstarted/what_is_uml.htm</a></p>
<p>Of course, It is not only my college that uses UML, there are a lot of company wich use UML tools in their development process, including  companies where I have worked and you can find some more examples <a href="http://www.uml.org/uml_success_stories/index.htm" target="_blank">here</a>.</p>
<h2>Umbrello</h2>
<p>So having a Free Software UML editor is pretty important! And the Umbrello UML editor is really cool:</p>
<ul>
<li>
Automatic code generation (Ada, C++, C#, Java, perl, PHP, Python, Ruby)</li>
<li>Import classes and project (Ada, C++, IDL, Java, Pascal and Python only)</li>
</ul>
<p>The  bad news is that Umbrello does not receive a lot of love. It has been  roughly ported to Qt4 and KDElibs4 but still uses a lot of Q3Canvas classes and has quite a few bugs.</p>
<p>[caption id="attachment_408" align="aligncenter" width="630" caption="Umbrello"]<a href="http://uml.sourceforge.net/"><img class="size-full wp-image-408 " title="Umbrello" src="/assets/images/diagram.png" alt="Umbrello today" width="630" height="369" /></a>[/caption]</p>
<h2>Working on Umbrello</h2>
<p>Which  is why I choose Umbrello for my conclusion work for the University. I  would have to work on something anyway, why not pick something that  matters? But as I combine my study (5 nights with each a different  class) with a full-time job I don't have a lot of  time to do a proper job on Umbrello. My goal for the University is  therefore pretty modest: I intend to finish the port of the canvas to  QGraphicsView. I have identified about 30 classes which are related to the Q3Canvas and will have to be ported or replaced. I also intend to use tools for automated tests, write unit tests and and fix some bugs.</p>
<div>But there is more to do:</div>
<ul>
<li>Better stereotypes supports</li>
<li>Complete Undo/Redo  support</li>
<li>Hyperlinks support</li>
<li>Reuse KDevelop analysis for code import
</li>
<li>Bug fixing</li>
</ul>
<h2>GSoC 2011</h2>
<p>So  I have applied for a Google Summer of Code. Jonathan Riddel, the  current maintainer of Umbrello, has said he would mentor me, which is  really cool. So if I get this, I can quit my current job and finish the  porting to QGraphicsView much faster. To ensure it'll be a successful  project, I've been quite modest in my goals for GSoC too: I only  shortened my university plan to the GSoC timeline and added a few small  things. If I finish the work for my conclusion work during the GSoC, I can be  more ambitious for my University and add to the plan - I'm sure my  professor won't mind if I take on some feature work in Umbrello as well!</p>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, Umbrello
date: "2011-04-05T23:36:45Z"
 
published: true
status: publish
tags: gsoc, kde, linkedin, umbrello
title: Building a sexy Umbrello


<p>I'm  a big fan of <a title="Umbrello" href="http://uml.sourceforge.net/" target="_blank">Umbrello</a>. It's a Free Software graphical <a title="UML" href="http://www.uml.org" target="_blank">UML</a> (Unified   Modeling Language) editor, one of the very few of it's kind. Most <a title="UML Tools" href="http://en.wikipedia.org/wiki/List_of_Unified_Modeling_Language_tools" target="_blank">UML tools are proprietary tools written in Java</a> and Umbrello is written in  C++/Qt and build on the powerful base of KDE  software. I realized how  interesting Umbrello is when I noticed that the  most of my professors  suggest proprietary tools or a <a href="http://projects.gnome.org/dia/" target="_blank">generic diagramming program with few UML features</a> to study UML at college class. Many companies use UML to help them quickly write applications and Umbrello is (as far as I know) the only Free Software tool which can do the code generation required for that!</p>
<h2>Why UML is important?</h2>
<p>"<em>Modeling  is the designing of software applications before coding. Modeling is an  Essential Part of large software projects, and helpful to medium and  even small projects as well. (...) Using a model, those responsible for a  software development project's success can assure themselves that  business functionality is complete and correct, end-user needs are met,  and program design supports requirements for scalability(...)</em>"<br />
<a href="http://www.omg.org/gettingstarted/what_is_uml.htm">http://www.omg.org/gettingstarted/what_is_uml.htm</a></p>
<p>Of course, It is not only my college that uses UML, there are a lot of company wich use UML tools in their development process, including  companies where I have worked and you can find some more examples <a href="http://www.uml.org/uml_success_stories/index.htm" target="_blank">here</a>.</p>
<h2>Umbrello</h2>
<p>So having a Free Software UML editor is pretty important! And the Umbrello UML editor is really cool:</p>
<ul>
<li>
Automatic code generation (Ada, C++, C#, Java, perl, PHP, Python, Ruby)</li>
<li>Import classes and project (Ada, C++, IDL, Java, Pascal and Python only)</li>
</ul>
<p>The  bad news is that Umbrello does not receive a lot of love. It has been  roughly ported to Qt4 and KDElibs4 but still uses a lot of Q3Canvas classes and has quite a few bugs.</p>
<p>[caption id="attachment_408" align="aligncenter" width="630" caption="Umbrello"]<a href="http://uml.sourceforge.net/"><img class="size-full wp-image-408 " title="Umbrello" src="/assets/images/diagram.png" alt="Umbrello today" width="630" height="369" /></a>[/caption]</p>
<h2>Working on Umbrello</h2>
<p>Which  is why I choose Umbrello for my conclusion work for the University. I  would have to work on something anyway, why not pick something that  matters? But as I combine my study (5 nights with each a different  class) with a full-time job I don't have a lot of  time to do a proper job on Umbrello. My goal for the University is  therefore pretty modest: I intend to finish the port of the canvas to  QGraphicsView. I have identified about 30 classes which are related to the Q3Canvas and will have to be ported or replaced. I also intend to use tools for automated tests, write unit tests and and fix some bugs.</p>
<div>But there is more to do:</div>
<ul>
<li>Better stereotypes supports</li>
<li>Complete Undo/Redo  support</li>
<li>Hyperlinks support</li>
<li>Reuse KDevelop analysis for code import
</li>
<li>Bug fixing</li>
</ul>
<h2>GSoC 2011</h2>
<p>So  I have applied for a Google Summer of Code. Jonathan Riddel, the  current maintainer of Umbrello, has said he would mentor me, which is  really cool. So if I get this, I can quit my current job and finish the  porting to QGraphicsView much faster. To ensure it'll be a successful  project, I've been quite modest in my goals for GSoC too: I only  shortened my university plan to the GSoC timeline and added a few small  things. If I finish the work for my conclusion work during the GSoC, I can be  more ambitious for my University and add to the plan - I'm sure my  professor won't mind if I take on some feature work in Umbrello as well!</p>
