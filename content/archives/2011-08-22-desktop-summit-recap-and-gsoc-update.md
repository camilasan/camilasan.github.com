
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, qt, Umbrello
date: "2011-08-22T12:51:22Z"
 
published: true
status: publish
tags: desktopsummit2011, gsoc, kde-br, linkedin, umbrello
title: Desktop Summit recap and GSoC update


<p><a href="http://s196.photobucket.com/albums/aa23/holymusic55/Blessings/?action=view&amp;current=BY284Home-is-Where-Your-Heart-is-Po.jpg&amp;sort=ascending"><img class="alignright" style="padding-bottom:15px;" title="Home is where the heart is" src="/assets/images/BY284Home-is-Where-Your-Heart-is-Po.jpg" alt="Home is where the heart is" width="110" height="114" /></a> After one week being at "home" (Brazil for a while) and getting back to the normal activities (college, clean up my place, cooking for myself..), now it is time to write something about the Desktop Summit and about the last weeks of GSoC.</p>
<h2 style="margin-top:15px;">Desktop Summit</h2>
<p>It was <strong>awesome</strong> because:</p>
<p><img class=" alignleft" style="float:left;padding-right:10px;margin:10px;" title="Friends!" src="/assets/images/6067518862_5030d0b818.jpg" alt="Brazil!" width="173" height="129" /></p>
<ul>
<li>It was really nice to see <strong>new brazilian people</strong> (good friends!) attending and doing good work for KDE. You can see pictures <a title="KDE Brazil" href="http://www.flickr.com/photos/kdebr/sets/72157627363477575/" target="_blank">here</a>.</li>
<li>Really good <strong>keynotes</strong>, like the <a href="http://www.asinen.org/" target="_blank">Stuart Jarvis's</a> about "<a href="https://desktopsummit.org/program/sessions/why-are-we-here" target="_blank">Why are we here? (Community Keynote)</a>". The graphics and the quotes in the slides were very intersting (they'll be put on the website soon).</li>
</ul>
<ul>
<li>I got a Tablet in the "<a href="http://appdeveloper.intel.com/events" target="_blank">Intel AppUp Application Lab for Meego</a>"! Good <strong>workshop</strong> and good Tablet =)</li>
<li>I attended in the <strong>BoF of KDE-Promo</strong> were Stuart Jarvis, Carl Symons, Frank Karlitschek , Thomas Thym and others discussed about the KDE birthday (october!) , about the KDE People from Latin America that should try to publish more news from these countries in the dot.kde.org (that's important!) and that we need more documentation about how to get more companies "involved" with KDE. (you can follow the <a href="https://mail.kde.org/mailman/listinfo/kde-promo" target="_blank">KDE Promo e-mail list</a> to know more)</li>
<li>I attended in the <a href="http://wiki.desktopsummit.org/Workshops_%26_BoFs/2011/Kolab_Groupware" target="_blank">Kolab: The Groupware for the Free Desktop BoF</a>, where I figured out that I need to study about KDE PIM ;-)<a href="http://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Mai_Tai.jpg/220px-Mai_Tai.jpg"><img class="alignright" title="Mai Tai" src="/assets/images/220px-Mai_Tai.jpg" alt="" width="68" height="103" /></a></li>
<li>I also figured out that <a href="http://en.wikipedia.org/wiki/Mai_Tai" target="_blank">Mai Tai</a> is really dangerous - don't drink more than two or you will<br />
try to hug and say how much you love people you never saw before!</li>
<li>I met <a href="http://jriddell.org/" target="_blank">Jonathan Riddell</a>in person, my GSoC Mentor.</li>
</ul>
<p>The <strong>only bad thing</strong> about Desktop Summit 2011:</p>
<ul>
<li>The potatoes were awesome, but the most of the dishes were with pork! I don't feel like eating pork meat for the rest for the year...</li>
</ul>
<h2>GSoC</h2>
<p>The <strong>difficulties</strong>:</p>
<ul>
<li>The <strong>lack of knowledge</strong> in C++/Qt. I didn't have a lot of experience with C++/Qt when I started which made me lose some time with stupid errors, but I believe I wasn't the only one with this problem in GSoC.</li>
<li>In the beginning I was afraid about the changes that I should do in Umbrello, how to do it properly, the best way to do it.</li>
<li>I took some time to <strong>communicate</strong> properly with my mentor. I shouldn't feel so insecure about it.</li>
<li>I didn't enjoy too much to work from home.</li>
<li>Concluding: my difficulties weren't so much about the code, but more <strong>personal difficulties</strong>. I think I wrote a ambitious project which would wait more dedication from me and I didn't give all the needed dedication. So I didn't conclude the project in time.</li>
</ul>
<p>What I did to <strong>overcome</strong> it:</p>
<ul>
<li><strong>Looking for help</strong>! Mainly from KDE people that I already knew in person.</li>
<li>With this help, I had <strong>good ideas</strong> about how to proceed properly with the port:  keep the old canvas working with the new canvas to keep comparing the code, using <a href="http://www.cplusplus.com/doc/tutorial/preprocessor/" target="_blank">preprocessor directives</a> in the old code and developing the new Umbrello in a different folder in the same project.</li>
<li>After the midterm evaluation I started to <strong>skype</strong> with my mentor.</li>
</ul>
<p>The project <strong>for now</strong>:</p>
<ul>
<li>I did start to <strong>merge</strong> my code in the trunk in a new branche: <a href="http://websvn.kde.org/branches/work/umbrello-qgv-port/" target="_blank">http://websvn.kde.org/branches/work/umbrello-qgv-port/</a></li>
<li>I have the <strong>EntityWidget</strong> "working" with some bugs: <a href="http://websvn.kde.org/branches/work/soc-umbrello-2011/" target="_blank">http://websvn.kde.org/branches/work/soc-umbrello-2011/</a></li>
<li>And as I intended to do, I have <strong>the old canvas and new canvas</strong> working together as you can see in <a href="http://kders.wordpress.com/tag/gsoc-2/" target="_blank">my previous posts about the project</a>.</li>
<li>I planned to use Squish (Squish Community Edition – froglogic Squish), an software for <strong>automated GUI tests</strong>. I had some problems with this, because I was creating long tests, so the tool couldn't find all the objects from the script in the object library, but at the Desktop Summit I talked to and asked for help from <a href="http://blauzahl.livejournal.com/" target="_blank">blauzahl</a> (thanks!) and she gave some tips, like to create short and complexy tests and this useful link: <a href="http://kb.froglogic.com/display/KB/Squish+Knowledge+Base" target="_blank">http://kb.froglogic.com/display/KB/Squish+Knowledge+Base</a>. So now I know how to properly create tests and I can keep and execute my plan.</li>
</ul>
<p>The <strong>future</strong>:</p>
<ul>
<li>These months in the GSoC gave me a <strong>good knowledge</strong> base to keep working in the Umbrello Port as my conclusion work for college.</li>
<li>We had a suggestion  how to change the <strong>documentation support</strong> works in Umbrello: <a href="http://people.canonical.com/%7Ejriddell/tmp/umbrelloDoc.pdf" target="_blank">http://people.canonical.com/~jriddell/tmp/umbrelloDoc.pdf</a></li>
<li>And soonish we will have the <strong>Qt 5</strong>, so we will have another port project for Umbrello (but as I was adviced, I should keep with the work to port for QT 4 because the differences to Qt 5 won't be so big)</li>
<li>And there is others suggestions about how to make the Umbrello <strong>interface</strong> better and with more <strong>usability</strong>.<br />
(you can follow it in the<a href="http://uml.sourceforge.net/contact.php" target="_blank"> uml devel mail list</a>)</li>
<li>Migrate Umbrello to git.</li>
<li>Write tests using <a href="http://doc.qt.nokia.com/latest/qtestlib-manual.html" target="_blank">QtestLib</a>.</li>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, qt, Umbrello
date: "2011-08-22T12:51:22Z"
 
published: true
status: publish
tags: desktopsummit2011, gsoc, kde-br, linkedin, umbrello
title: Desktop Summit recap and GSoC update


<p><a href="http://s196.photobucket.com/albums/aa23/holymusic55/Blessings/?action=view&amp;current=BY284Home-is-Where-Your-Heart-is-Po.jpg&amp;sort=ascending"><img class="alignright" style="padding-bottom:15px;" title="Home is where the heart is" src="/assets/images/BY284Home-is-Where-Your-Heart-is-Po.jpg" alt="Home is where the heart is" width="110" height="114" /></a> After one week being at "home" (Brazil for a while) and getting back to the normal activities (college, clean up my place, cooking for myself..), now it is time to write something about the Desktop Summit and about the last weeks of GSoC.</p>
<h2 style="margin-top:15px;">Desktop Summit</h2>
<p>It was <strong>awesome</strong> because:</p>
<p><img class=" alignleft" style="float:left;padding-right:10px;margin:10px;" title="Friends!" src="/assets/images/6067518862_5030d0b818.jpg" alt="Brazil!" width="173" height="129" /></p>
<ul>
<li>It was really nice to see <strong>new brazilian people</strong> (good friends!) attending and doing good work for KDE. You can see pictures <a title="KDE Brazil" href="http://www.flickr.com/photos/kdebr/sets/72157627363477575/" target="_blank">here</a>.</li>
<li>Really good <strong>keynotes</strong>, like the <a href="http://www.asinen.org/" target="_blank">Stuart Jarvis's</a> about "<a href="https://desktopsummit.org/program/sessions/why-are-we-here" target="_blank">Why are we here? (Community Keynote)</a>". The graphics and the quotes in the slides were very intersting (they'll be put on the website soon).</li>
</ul>
<ul>
<li>I got a Tablet in the "<a href="http://appdeveloper.intel.com/events" target="_blank">Intel AppUp Application Lab for Meego</a>"! Good <strong>workshop</strong> and good Tablet =)</li>
<li>I attended in the <strong>BoF of KDE-Promo</strong> were Stuart Jarvis, Carl Symons, Frank Karlitschek , Thomas Thym and others discussed about the KDE birthday (october!) , about the KDE People from Latin America that should try to publish more news from these countries in the dot.kde.org (that's important!) and that we need more documentation about how to get more companies "involved" with KDE. (you can follow the <a href="https://mail.kde.org/mailman/listinfo/kde-promo" target="_blank">KDE Promo e-mail list</a> to know more)</li>
<li>I attended in the <a href="http://wiki.desktopsummit.org/Workshops_%26_BoFs/2011/Kolab_Groupware" target="_blank">Kolab: The Groupware for the Free Desktop BoF</a>, where I figured out that I need to study about KDE PIM ;-)<a href="http://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Mai_Tai.jpg/220px-Mai_Tai.jpg"><img class="alignright" title="Mai Tai" src="/assets/images/220px-Mai_Tai.jpg" alt="" width="68" height="103" /></a></li>
<li>I also figured out that <a href="http://en.wikipedia.org/wiki/Mai_Tai" target="_blank">Mai Tai</a> is really dangerous - don't drink more than two or you will<br />
try to hug and say how much you love people you never saw before!</li>
<li>I met <a href="http://jriddell.org/" target="_blank">Jonathan Riddell</a>in person, my GSoC Mentor.</li>
</ul>
<p>The <strong>only bad thing</strong> about Desktop Summit 2011:</p>
<ul>
<li>The potatoes were awesome, but the most of the dishes were with pork! I don't feel like eating pork meat for the rest for the year...</li>
</ul>
<h2>GSoC</h2>
<p>The <strong>difficulties</strong>:</p>
<ul>
<li>The <strong>lack of knowledge</strong> in C++/Qt. I didn't have a lot of experience with C++/Qt when I started which made me lose some time with stupid errors, but I believe I wasn't the only one with this problem in GSoC.</li>
<li>In the beginning I was afraid about the changes that I should do in Umbrello, how to do it properly, the best way to do it.</li>
<li>I took some time to <strong>communicate</strong> properly with my mentor. I shouldn't feel so insecure about it.</li>
<li>I didn't enjoy too much to work from home.</li>
<li>Concluding: my difficulties weren't so much about the code, but more <strong>personal difficulties</strong>. I think I wrote a ambitious project which would wait more dedication from me and I didn't give all the needed dedication. So I didn't conclude the project in time.</li>
</ul>
<p>What I did to <strong>overcome</strong> it:</p>
<ul>
<li><strong>Looking for help</strong>! Mainly from KDE people that I already knew in person.</li>
<li>With this help, I had <strong>good ideas</strong> about how to proceed properly with the port:  keep the old canvas working with the new canvas to keep comparing the code, using <a href="http://www.cplusplus.com/doc/tutorial/preprocessor/" target="_blank">preprocessor directives</a> in the old code and developing the new Umbrello in a different folder in the same project.</li>
<li>After the midterm evaluation I started to <strong>skype</strong> with my mentor.</li>
</ul>
<p>The project <strong>for now</strong>:</p>
<ul>
<li>I did start to <strong>merge</strong> my code in the trunk in a new branche: <a href="http://websvn.kde.org/branches/work/umbrello-qgv-port/" target="_blank">http://websvn.kde.org/branches/work/umbrello-qgv-port/</a></li>
<li>I have the <strong>EntityWidget</strong> "working" with some bugs: <a href="http://websvn.kde.org/branches/work/soc-umbrello-2011/" target="_blank">http://websvn.kde.org/branches/work/soc-umbrello-2011/</a></li>
<li>And as I intended to do, I have <strong>the old canvas and new canvas</strong> working together as you can see in <a href="http://kders.wordpress.com/tag/gsoc-2/" target="_blank">my previous posts about the project</a>.</li>
<li>I planned to use Squish (Squish Community Edition – froglogic Squish), an software for <strong>automated GUI tests</strong>. I had some problems with this, because I was creating long tests, so the tool couldn't find all the objects from the script in the object library, but at the Desktop Summit I talked to and asked for help from <a href="http://blauzahl.livejournal.com/" target="_blank">blauzahl</a> (thanks!) and she gave some tips, like to create short and complexy tests and this useful link: <a href="http://kb.froglogic.com/display/KB/Squish+Knowledge+Base" target="_blank">http://kb.froglogic.com/display/KB/Squish+Knowledge+Base</a>. So now I know how to properly create tests and I can keep and execute my plan.</li>
</ul>
<p>The <strong>future</strong>:</p>
<ul>
<li>These months in the GSoC gave me a <strong>good knowledge</strong> base to keep working in the Umbrello Port as my conclusion work for college.</li>
<li>We had a suggestion  how to change the <strong>documentation support</strong> works in Umbrello: <a href="http://people.canonical.com/%7Ejriddell/tmp/umbrelloDoc.pdf" target="_blank">http://people.canonical.com/~jriddell/tmp/umbrelloDoc.pdf</a></li>
<li>And soonish we will have the <strong>Qt 5</strong>, so we will have another port project for Umbrello (but as I was adviced, I should keep with the work to port for QT 4 because the differences to Qt 5 won't be so big)</li>
<li>And there is others suggestions about how to make the Umbrello <strong>interface</strong> better and with more <strong>usability</strong>.<br />
(you can follow it in the<a href="http://uml.sourceforge.net/contact.php" target="_blank"> uml devel mail list</a>)</li>
<li>Migrate Umbrello to git.</li>
<li>Write tests using <a href="http://doc.qt.nokia.com/latest/qtestlib-manual.html" target="_blank">QtestLib</a>.</li>
</ul>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, qt, Umbrello
date: "2011-08-22T12:51:22Z"
 
published: true
status: publish
tags: desktopsummit2011, gsoc, kde-br, linkedin, umbrello
title: Desktop Summit recap and GSoC update


<p><a href="http://s196.photobucket.com/albums/aa23/holymusic55/Blessings/?action=view&amp;current=BY284Home-is-Where-Your-Heart-is-Po.jpg&amp;sort=ascending"><img class="alignright" style="padding-bottom:15px;" title="Home is where the heart is" src="/assets/images/BY284Home-is-Where-Your-Heart-is-Po.jpg" alt="Home is where the heart is" width="110" height="114" /></a> After one week being at "home" (Brazil for a while) and getting back to the normal activities (college, clean up my place, cooking for myself..), now it is time to write something about the Desktop Summit and about the last weeks of GSoC.</p>
<h2 style="margin-top:15px;">Desktop Summit</h2>
<p>It was <strong>awesome</strong> because:</p>
<p><img class=" alignleft" style="float:left;padding-right:10px;margin:10px;" title="Friends!" src="/assets/images/6067518862_5030d0b818.jpg" alt="Brazil!" width="173" height="129" /></p>
<ul>
<li>It was really nice to see <strong>new brazilian people</strong> (good friends!) attending and doing good work for KDE. You can see pictures <a title="KDE Brazil" href="http://www.flickr.com/photos/kdebr/sets/72157627363477575/" target="_blank">here</a>.</li>
<li>Really good <strong>keynotes</strong>, like the <a href="http://www.asinen.org/" target="_blank">Stuart Jarvis's</a> about "<a href="https://desktopsummit.org/program/sessions/why-are-we-here" target="_blank">Why are we here? (Community Keynote)</a>". The graphics and the quotes in the slides were very intersting (they'll be put on the website soon).</li>
</ul>
<ul>
<li>I got a Tablet in the "<a href="http://appdeveloper.intel.com/events" target="_blank">Intel AppUp Application Lab for Meego</a>"! Good <strong>workshop</strong> and good Tablet =)</li>
<li>I attended in the <strong>BoF of KDE-Promo</strong> were Stuart Jarvis, Carl Symons, Frank Karlitschek , Thomas Thym and others discussed about the KDE birthday (october!) , about the KDE People from Latin America that should try to publish more news from these countries in the dot.kde.org (that's important!) and that we need more documentation about how to get more companies "involved" with KDE. (you can follow the <a href="https://mail.kde.org/mailman/listinfo/kde-promo" target="_blank">KDE Promo e-mail list</a> to know more)</li>
<li>I attended in the <a href="http://wiki.desktopsummit.org/Workshops_%26_BoFs/2011/Kolab_Groupware" target="_blank">Kolab: The Groupware for the Free Desktop BoF</a>, where I figured out that I need to study about KDE PIM ;-)<a href="http://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Mai_Tai.jpg/220px-Mai_Tai.jpg"><img class="alignright" title="Mai Tai" src="/assets/images/220px-Mai_Tai.jpg" alt="" width="68" height="103" /></a></li>
<li>I also figured out that <a href="http://en.wikipedia.org/wiki/Mai_Tai" target="_blank">Mai Tai</a> is really dangerous - don't drink more than two or you will<br />
try to hug and say how much you love people you never saw before!</li>
<li>I met <a href="http://jriddell.org/" target="_blank">Jonathan Riddell</a>in person, my GSoC Mentor.</li>
</ul>
<p>The <strong>only bad thing</strong> about Desktop Summit 2011:</p>
<ul>
<li>The potatoes were awesome, but the most of the dishes were with pork! I don't feel like eating pork meat for the rest for the year...</li>
</ul>
<h2>GSoC</h2>
<p>The <strong>difficulties</strong>:</p>
<ul>
<li>The <strong>lack of knowledge</strong> in C++/Qt. I didn't have a lot of experience with C++/Qt when I started which made me lose some time with stupid errors, but I believe I wasn't the only one with this problem in GSoC.</li>
<li>In the beginning I was afraid about the changes that I should do in Umbrello, how to do it properly, the best way to do it.</li>
<li>I took some time to <strong>communicate</strong> properly with my mentor. I shouldn't feel so insecure about it.</li>
<li>I didn't enjoy too much to work from home.</li>
<li>Concluding: my difficulties weren't so much about the code, but more <strong>personal difficulties</strong>. I think I wrote a ambitious project which would wait more dedication from me and I didn't give all the needed dedication. So I didn't conclude the project in time.</li>
</ul>
<p>What I did to <strong>overcome</strong> it:</p>
<ul>
<li><strong>Looking for help</strong>! Mainly from KDE people that I already knew in person.</li>
<li>With this help, I had <strong>good ideas</strong> about how to proceed properly with the port:  keep the old canvas working with the new canvas to keep comparing the code, using <a href="http://www.cplusplus.com/doc/tutorial/preprocessor/" target="_blank">preprocessor directives</a> in the old code and developing the new Umbrello in a different folder in the same project.</li>
<li>After the midterm evaluation I started to <strong>skype</strong> with my mentor.</li>
</ul>
<p>The project <strong>for now</strong>:</p>
<ul>
<li>I did start to <strong>merge</strong> my code in the trunk in a new branche: <a href="http://websvn.kde.org/branches/work/umbrello-qgv-port/" target="_blank">http://websvn.kde.org/branches/work/umbrello-qgv-port/</a></li>
<li>I have the <strong>EntityWidget</strong> "working" with some bugs: <a href="http://websvn.kde.org/branches/work/soc-umbrello-2011/" target="_blank">http://websvn.kde.org/branches/work/soc-umbrello-2011/</a></li>
<li>And as I intended to do, I have <strong>the old canvas and new canvas</strong> working together as you can see in <a href="http://kders.wordpress.com/tag/gsoc-2/" target="_blank">my previous posts about the project</a>.</li>
<li>I planned to use Squish (Squish Community Edition – froglogic Squish), an software for <strong>automated GUI tests</strong>. I had some problems with this, because I was creating long tests, so the tool couldn't find all the objects from the script in the object library, but at the Desktop Summit I talked to and asked for help from <a href="http://blauzahl.livejournal.com/" target="_blank">blauzahl</a> (thanks!) and she gave some tips, like to create short and complexy tests and this useful link: <a href="http://kb.froglogic.com/display/KB/Squish+Knowledge+Base" target="_blank">http://kb.froglogic.com/display/KB/Squish+Knowledge+Base</a>. So now I know how to properly create tests and I can keep and execute my plan.</li>
</ul>
<p>The <strong>future</strong>:</p>
<ul>
<li>These months in the GSoC gave me a <strong>good knowledge</strong> base to keep working in the Umbrello Port as my conclusion work for college.</li>
<li>We had a suggestion  how to change the <strong>documentation support</strong> works in Umbrello: <a href="http://people.canonical.com/%7Ejriddell/tmp/umbrelloDoc.pdf" target="_blank">http://people.canonical.com/~jriddell/tmp/umbrelloDoc.pdf</a></li>
<li>And soonish we will have the <strong>Qt 5</strong>, so we will have another port project for Umbrello (but as I was adviced, I should keep with the work to port for QT 4 because the differences to Qt 5 won't be so big)</li>
<li>And there is others suggestions about how to make the Umbrello <strong>interface</strong> better and with more <strong>usability</strong>.<br />
(you can follow it in the<a href="http://uml.sourceforge.net/contact.php" target="_blank"> uml devel mail list</a>)</li>
<li>Migrate Umbrello to git.</li>
<li>Write tests using <a href="http://doc.qt.nokia.com/latest/qtestlib-manual.html" target="_blank">QtestLib</a>.</li>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, qt, Umbrello
date: "2011-08-22T12:51:22Z"
 
published: true
status: publish
tags: desktopsummit2011, gsoc, kde-br, linkedin, umbrello
title: Desktop Summit recap and GSoC update


<p><a href="http://s196.photobucket.com/albums/aa23/holymusic55/Blessings/?action=view&amp;current=BY284Home-is-Where-Your-Heart-is-Po.jpg&amp;sort=ascending"><img class="alignright" style="padding-bottom:15px;" title="Home is where the heart is" src="/assets/images/BY284Home-is-Where-Your-Heart-is-Po.jpg" alt="Home is where the heart is" width="110" height="114" /></a> After one week being at "home" (Brazil for a while) and getting back to the normal activities (college, clean up my place, cooking for myself..), now it is time to write something about the Desktop Summit and about the last weeks of GSoC.</p>
<h2 style="margin-top:15px;">Desktop Summit</h2>
<p>It was <strong>awesome</strong> because:</p>
<p><img class=" alignleft" style="float:left;padding-right:10px;margin:10px;" title="Friends!" src="/assets/images/6067518862_5030d0b818.jpg" alt="Brazil!" width="173" height="129" /></p>
<ul>
<li>It was really nice to see <strong>new brazilian people</strong> (good friends!) attending and doing good work for KDE. You can see pictures <a title="KDE Brazil" href="http://www.flickr.com/photos/kdebr/sets/72157627363477575/" target="_blank">here</a>.</li>
<li>Really good <strong>keynotes</strong>, like the <a href="http://www.asinen.org/" target="_blank">Stuart Jarvis's</a> about "<a href="https://desktopsummit.org/program/sessions/why-are-we-here" target="_blank">Why are we here? (Community Keynote)</a>". The graphics and the quotes in the slides were very intersting (they'll be put on the website soon).</li>
</ul>
<ul>
<li>I got a Tablet in the "<a href="http://appdeveloper.intel.com/events" target="_blank">Intel AppUp Application Lab for Meego</a>"! Good <strong>workshop</strong> and good Tablet =)</li>
<li>I attended in the <strong>BoF of KDE-Promo</strong> were Stuart Jarvis, Carl Symons, Frank Karlitschek , Thomas Thym and others discussed about the KDE birthday (october!) , about the KDE People from Latin America that should try to publish more news from these countries in the dot.kde.org (that's important!) and that we need more documentation about how to get more companies "involved" with KDE. (you can follow the <a href="https://mail.kde.org/mailman/listinfo/kde-promo" target="_blank">KDE Promo e-mail list</a> to know more)</li>
<li>I attended in the <a href="http://wiki.desktopsummit.org/Workshops_%26_BoFs/2011/Kolab_Groupware" target="_blank">Kolab: The Groupware for the Free Desktop BoF</a>, where I figured out that I need to study about KDE PIM ;-)<a href="http://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Mai_Tai.jpg/220px-Mai_Tai.jpg"><img class="alignright" title="Mai Tai" src="/assets/images/220px-Mai_Tai.jpg" alt="" width="68" height="103" /></a></li>
<li>I also figured out that <a href="http://en.wikipedia.org/wiki/Mai_Tai" target="_blank">Mai Tai</a> is really dangerous - don't drink more than two or you will<br />
try to hug and say how much you love people you never saw before!</li>
<li>I met <a href="http://jriddell.org/" target="_blank">Jonathan Riddell</a>in person, my GSoC Mentor.</li>
</ul>
<p>The <strong>only bad thing</strong> about Desktop Summit 2011:</p>
<ul>
<li>The potatoes were awesome, but the most of the dishes were with pork! I don't feel like eating pork meat for the rest for the year...</li>
</ul>
<h2>GSoC</h2>
<p>The <strong>difficulties</strong>:</p>
<ul>
<li>The <strong>lack of knowledge</strong> in C++/Qt. I didn't have a lot of experience with C++/Qt when I started which made me lose some time with stupid errors, but I believe I wasn't the only one with this problem in GSoC.</li>
<li>In the beginning I was afraid about the changes that I should do in Umbrello, how to do it properly, the best way to do it.</li>
<li>I took some time to <strong>communicate</strong> properly with my mentor. I shouldn't feel so insecure about it.</li>
<li>I didn't enjoy too much to work from home.</li>
<li>Concluding: my difficulties weren't so much about the code, but more <strong>personal difficulties</strong>. I think I wrote a ambitious project which would wait more dedication from me and I didn't give all the needed dedication. So I didn't conclude the project in time.</li>
</ul>
<p>What I did to <strong>overcome</strong> it:</p>
<ul>
<li><strong>Looking for help</strong>! Mainly from KDE people that I already knew in person.</li>
<li>With this help, I had <strong>good ideas</strong> about how to proceed properly with the port:  keep the old canvas working with the new canvas to keep comparing the code, using <a href="http://www.cplusplus.com/doc/tutorial/preprocessor/" target="_blank">preprocessor directives</a> in the old code and developing the new Umbrello in a different folder in the same project.</li>
<li>After the midterm evaluation I started to <strong>skype</strong> with my mentor.</li>
</ul>
<p>The project <strong>for now</strong>:</p>
<ul>
<li>I did start to <strong>merge</strong> my code in the trunk in a new branche: <a href="http://websvn.kde.org/branches/work/umbrello-qgv-port/" target="_blank">http://websvn.kde.org/branches/work/umbrello-qgv-port/</a></li>
<li>I have the <strong>EntityWidget</strong> "working" with some bugs: <a href="http://websvn.kde.org/branches/work/soc-umbrello-2011/" target="_blank">http://websvn.kde.org/branches/work/soc-umbrello-2011/</a></li>
<li>And as I intended to do, I have <strong>the old canvas and new canvas</strong> working together as you can see in <a href="http://kders.wordpress.com/tag/gsoc-2/" target="_blank">my previous posts about the project</a>.</li>
<li>I planned to use Squish (Squish Community Edition – froglogic Squish), an software for <strong>automated GUI tests</strong>. I had some problems with this, because I was creating long tests, so the tool couldn't find all the objects from the script in the object library, but at the Desktop Summit I talked to and asked for help from <a href="http://blauzahl.livejournal.com/" target="_blank">blauzahl</a> (thanks!) and she gave some tips, like to create short and complexy tests and this useful link: <a href="http://kb.froglogic.com/display/KB/Squish+Knowledge+Base" target="_blank">http://kb.froglogic.com/display/KB/Squish+Knowledge+Base</a>. So now I know how to properly create tests and I can keep and execute my plan.</li>
</ul>
<p>The <strong>future</strong>:</p>
<ul>
<li>These months in the GSoC gave me a <strong>good knowledge</strong> base to keep working in the Umbrello Port as my conclusion work for college.</li>
<li>We had a suggestion  how to change the <strong>documentation support</strong> works in Umbrello: <a href="http://people.canonical.com/%7Ejriddell/tmp/umbrelloDoc.pdf" target="_blank">http://people.canonical.com/~jriddell/tmp/umbrelloDoc.pdf</a></li>
<li>And soonish we will have the <strong>Qt 5</strong>, so we will have another port project for Umbrello (but as I was adviced, I should keep with the work to port for QT 4 because the differences to Qt 5 won't be so big)</li>
<li>And there is others suggestions about how to make the Umbrello <strong>interface</strong> better and with more <strong>usability</strong>.<br />
(you can follow it in the<a href="http://uml.sourceforge.net/contact.php" target="_blank"> uml devel mail list</a>)</li>
<li>Migrate Umbrello to git.</li>
<li>Write tests using <a href="http://doc.qt.nokia.com/latest/qtestlib-manual.html" target="_blank">QtestLib</a>.</li>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, qt, Umbrello
date: "2011-08-22T12:51:22Z"
 
published: true
status: publish
tags: desktopsummit2011, gsoc, kde-br, linkedin, umbrello
title: Desktop Summit recap and GSoC update


<p><a href="http://s196.photobucket.com/albums/aa23/holymusic55/Blessings/?action=view&amp;current=BY284Home-is-Where-Your-Heart-is-Po.jpg&amp;sort=ascending"><img class="alignright" style="padding-bottom:15px;" title="Home is where the heart is" src="/assets/images/BY284Home-is-Where-Your-Heart-is-Po.jpg" alt="Home is where the heart is" width="110" height="114" /></a> After one week being at "home" (Brazil for a while) and getting back to the normal activities (college, clean up my place, cooking for myself..), now it is time to write something about the Desktop Summit and about the last weeks of GSoC.</p>
<h2 style="margin-top:15px;">Desktop Summit</h2>
<p>It was <strong>awesome</strong> because:</p>
<p><img class=" alignleft" style="float:left;padding-right:10px;margin:10px;" title="Friends!" src="/assets/images/6067518862_5030d0b818.jpg" alt="Brazil!" width="173" height="129" /></p>
<ul>
<li>It was really nice to see <strong>new brazilian people</strong> (good friends!) attending and doing good work for KDE. You can see pictures <a title="KDE Brazil" href="http://www.flickr.com/photos/kdebr/sets/72157627363477575/" target="_blank">here</a>.</li>
<li>Really good <strong>keynotes</strong>, like the <a href="http://www.asinen.org/" target="_blank">Stuart Jarvis's</a> about "<a href="https://desktopsummit.org/program/sessions/why-are-we-here" target="_blank">Why are we here? (Community Keynote)</a>". The graphics and the quotes in the slides were very intersting (they'll be put on the website soon).</li>
</ul>
<ul>
<li>I got a Tablet in the "<a href="http://appdeveloper.intel.com/events" target="_blank">Intel AppUp Application Lab for Meego</a>"! Good <strong>workshop</strong> and good Tablet =)</li>
<li>I attended in the <strong>BoF of KDE-Promo</strong> were Stuart Jarvis, Carl Symons, Frank Karlitschek , Thomas Thym and others discussed about the KDE birthday (october!) , about the KDE People from Latin America that should try to publish more news from these countries in the dot.kde.org (that's important!) and that we need more documentation about how to get more companies "involved" with KDE. (you can follow the <a href="https://mail.kde.org/mailman/listinfo/kde-promo" target="_blank">KDE Promo e-mail list</a> to know more)</li>
<li>I attended in the <a href="http://wiki.desktopsummit.org/Workshops_%26_BoFs/2011/Kolab_Groupware" target="_blank">Kolab: The Groupware for the Free Desktop BoF</a>, where I figured out that I need to study about KDE PIM ;-)<a href="http://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Mai_Tai.jpg/220px-Mai_Tai.jpg"><img class="alignright" title="Mai Tai" src="/assets/images/220px-Mai_Tai.jpg" alt="" width="68" height="103" /></a></li>
<li>I also figured out that <a href="http://en.wikipedia.org/wiki/Mai_Tai" target="_blank">Mai Tai</a> is really dangerous - don't drink more than two or you will<br />
try to hug and say how much you love people you never saw before!</li>
<li>I met <a href="http://jriddell.org/" target="_blank">Jonathan Riddell</a>in person, my GSoC Mentor.</li>
</ul>
<p>The <strong>only bad thing</strong> about Desktop Summit 2011:</p>
<ul>
<li>The potatoes were awesome, but the most of the dishes were with pork! I don't feel like eating pork meat for the rest for the year...</li>
</ul>
<h2>GSoC</h2>
<p>The <strong>difficulties</strong>:</p>
<ul>
<li>The <strong>lack of knowledge</strong> in C++/Qt. I didn't have a lot of experience with C++/Qt when I started which made me lose some time with stupid errors, but I believe I wasn't the only one with this problem in GSoC.</li>
<li>In the beginning I was afraid about the changes that I should do in Umbrello, how to do it properly, the best way to do it.</li>
<li>I took some time to <strong>communicate</strong> properly with my mentor. I shouldn't feel so insecure about it.</li>
<li>I didn't enjoy too much to work from home.</li>
<li>Concluding: my difficulties weren't so much about the code, but more <strong>personal difficulties</strong>. I think I wrote a ambitious project which would wait more dedication from me and I didn't give all the needed dedication. So I didn't conclude the project in time.</li>
</ul>
<p>What I did to <strong>overcome</strong> it:</p>
<ul>
<li><strong>Looking for help</strong>! Mainly from KDE people that I already knew in person.</li>
<li>With this help, I had <strong>good ideas</strong> about how to proceed properly with the port:  keep the old canvas working with the new canvas to keep comparing the code, using <a href="http://www.cplusplus.com/doc/tutorial/preprocessor/" target="_blank">preprocessor directives</a> in the old code and developing the new Umbrello in a different folder in the same project.</li>
<li>After the midterm evaluation I started to <strong>skype</strong> with my mentor.</li>
</ul>
<p>The project <strong>for now</strong>:</p>
<ul>
<li>I did start to <strong>merge</strong> my code in the trunk in a new branche: <a href="http://websvn.kde.org/branches/work/umbrello-qgv-port/" target="_blank">http://websvn.kde.org/branches/work/umbrello-qgv-port/</a></li>
<li>I have the <strong>EntityWidget</strong> "working" with some bugs: <a href="http://websvn.kde.org/branches/work/soc-umbrello-2011/" target="_blank">http://websvn.kde.org/branches/work/soc-umbrello-2011/</a></li>
<li>And as I intended to do, I have <strong>the old canvas and new canvas</strong> working together as you can see in <a href="http://kders.wordpress.com/tag/gsoc-2/" target="_blank">my previous posts about the project</a>.</li>
<li>I planned to use Squish (Squish Community Edition – froglogic Squish), an software for <strong>automated GUI tests</strong>. I had some problems with this, because I was creating long tests, so the tool couldn't find all the objects from the script in the object library, but at the Desktop Summit I talked to and asked for help from <a href="http://blauzahl.livejournal.com/" target="_blank">blauzahl</a> (thanks!) and she gave some tips, like to create short and complexy tests and this useful link: <a href="http://kb.froglogic.com/display/KB/Squish+Knowledge+Base" target="_blank">http://kb.froglogic.com/display/KB/Squish+Knowledge+Base</a>. So now I know how to properly create tests and I can keep and execute my plan.</li>
</ul>
<p>The <strong>future</strong>:</p>
<ul>
<li>These months in the GSoC gave me a <strong>good knowledge</strong> base to keep working in the Umbrello Port as my conclusion work for college.</li>
<li>We had a suggestion  how to change the <strong>documentation support</strong> works in Umbrello: <a href="http://people.canonical.com/%7Ejriddell/tmp/umbrelloDoc.pdf" target="_blank">http://people.canonical.com/~jriddell/tmp/umbrelloDoc.pdf</a></li>
<li>And soonish we will have the <strong>Qt 5</strong>, so we will have another port project for Umbrello (but as I was adviced, I should keep with the work to port for QT 4 because the differences to Qt 5 won't be so big)</li>
<li>And there is others suggestions about how to make the Umbrello <strong>interface</strong> better and with more <strong>usability</strong>.<br />
(you can follow it in the<a href="http://uml.sourceforge.net/contact.php" target="_blank"> uml devel mail list</a>)</li>
<li>Migrate Umbrello to git.</li>
<li>Write tests using <a href="http://doc.qt.nokia.com/latest/qtestlib-manual.html" target="_blank">QtestLib</a>.</li>
</ul>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, qt, Umbrello
date: "2011-08-22T12:51:22Z"
 
published: true
status: publish
tags: desktopsummit2011, gsoc, kde-br, linkedin, umbrello
title: Desktop Summit recap and GSoC update


<p><a href="http://s196.photobucket.com/albums/aa23/holymusic55/Blessings/?action=view&amp;current=BY284Home-is-Where-Your-Heart-is-Po.jpg&amp;sort=ascending"><img class="alignright" style="padding-bottom:15px;" title="Home is where the heart is" src="/assets/images/BY284Home-is-Where-Your-Heart-is-Po.jpg" alt="Home is where the heart is" width="110" height="114" /></a> After one week being at "home" (Brazil for a while) and getting back to the normal activities (college, clean up my place, cooking for myself..), now it is time to write something about the Desktop Summit and about the last weeks of GSoC.</p>
<h2 style="margin-top:15px;">Desktop Summit</h2>
<p>It was <strong>awesome</strong> because:</p>
<p><img class=" alignleft" style="float:left;padding-right:10px;margin:10px;" title="Friends!" src="/assets/images/6067518862_5030d0b818.jpg" alt="Brazil!" width="173" height="129" /></p>
<ul>
<li>It was really nice to see <strong>new brazilian people</strong> (good friends!) attending and doing good work for KDE. You can see pictures <a title="KDE Brazil" href="http://www.flickr.com/photos/kdebr/sets/72157627363477575/" target="_blank">here</a>.</li>
<li>Really good <strong>keynotes</strong>, like the <a href="http://www.asinen.org/" target="_blank">Stuart Jarvis's</a> about "<a href="https://desktopsummit.org/program/sessions/why-are-we-here" target="_blank">Why are we here? (Community Keynote)</a>". The graphics and the quotes in the slides were very intersting (they'll be put on the website soon).</li>
</ul>
<ul>
<li>I got a Tablet in the "<a href="http://appdeveloper.intel.com/events" target="_blank">Intel AppUp Application Lab for Meego</a>"! Good <strong>workshop</strong> and good Tablet =)</li>
<li>I attended in the <strong>BoF of KDE-Promo</strong> were Stuart Jarvis, Carl Symons, Frank Karlitschek , Thomas Thym and others discussed about the KDE birthday (october!) , about the KDE People from Latin America that should try to publish more news from these countries in the dot.kde.org (that's important!) and that we need more documentation about how to get more companies "involved" with KDE. (you can follow the <a href="https://mail.kde.org/mailman/listinfo/kde-promo" target="_blank">KDE Promo e-mail list</a> to know more)</li>
<li>I attended in the <a href="http://wiki.desktopsummit.org/Workshops_%26_BoFs/2011/Kolab_Groupware" target="_blank">Kolab: The Groupware for the Free Desktop BoF</a>, where I figured out that I need to study about KDE PIM ;-)<a href="http://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Mai_Tai.jpg/220px-Mai_Tai.jpg"><img class="alignright" title="Mai Tai" src="/assets/images/220px-Mai_Tai.jpg" alt="" width="68" height="103" /></a></li>
<li>I also figured out that <a href="http://en.wikipedia.org/wiki/Mai_Tai" target="_blank">Mai Tai</a> is really dangerous - don't drink more than two or you will<br />
try to hug and say how much you love people you never saw before!</li>
<li>I met <a href="http://jriddell.org/" target="_blank">Jonathan Riddell</a>in person, my GSoC Mentor.</li>
</ul>
<p>The <strong>only bad thing</strong> about Desktop Summit 2011:</p>
<ul>
<li>The potatoes were awesome, but the most of the dishes were with pork! I don't feel like eating pork meat for the rest for the year...</li>
</ul>
<h2>GSoC</h2>
<p>The <strong>difficulties</strong>:</p>
<ul>
<li>The <strong>lack of knowledge</strong> in C++/Qt. I didn't have a lot of experience with C++/Qt when I started which made me lose some time with stupid errors, but I believe I wasn't the only one with this problem in GSoC.</li>
<li>In the beginning I was afraid about the changes that I should do in Umbrello, how to do it properly, the best way to do it.</li>
<li>I took some time to <strong>communicate</strong> properly with my mentor. I shouldn't feel so insecure about it.</li>
<li>I didn't enjoy too much to work from home.</li>
<li>Concluding: my difficulties weren't so much about the code, but more <strong>personal difficulties</strong>. I think I wrote a ambitious project which would wait more dedication from me and I didn't give all the needed dedication. So I didn't conclude the project in time.</li>
</ul>
<p>What I did to <strong>overcome</strong> it:</p>
<ul>
<li><strong>Looking for help</strong>! Mainly from KDE people that I already knew in person.</li>
<li>With this help, I had <strong>good ideas</strong> about how to proceed properly with the port:  keep the old canvas working with the new canvas to keep comparing the code, using <a href="http://www.cplusplus.com/doc/tutorial/preprocessor/" target="_blank">preprocessor directives</a> in the old code and developing the new Umbrello in a different folder in the same project.</li>
<li>After the midterm evaluation I started to <strong>skype</strong> with my mentor.</li>
</ul>
<p>The project <strong>for now</strong>:</p>
<ul>
<li>I did start to <strong>merge</strong> my code in the trunk in a new branche: <a href="http://websvn.kde.org/branches/work/umbrello-qgv-port/" target="_blank">http://websvn.kde.org/branches/work/umbrello-qgv-port/</a></li>
<li>I have the <strong>EntityWidget</strong> "working" with some bugs: <a href="http://websvn.kde.org/branches/work/soc-umbrello-2011/" target="_blank">http://websvn.kde.org/branches/work/soc-umbrello-2011/</a></li>
<li>And as I intended to do, I have <strong>the old canvas and new canvas</strong> working together as you can see in <a href="http://kders.wordpress.com/tag/gsoc-2/" target="_blank">my previous posts about the project</a>.</li>
<li>I planned to use Squish (Squish Community Edition – froglogic Squish), an software for <strong>automated GUI tests</strong>. I had some problems with this, because I was creating long tests, so the tool couldn't find all the objects from the script in the object library, but at the Desktop Summit I talked to and asked for help from <a href="http://blauzahl.livejournal.com/" target="_blank">blauzahl</a> (thanks!) and she gave some tips, like to create short and complexy tests and this useful link: <a href="http://kb.froglogic.com/display/KB/Squish+Knowledge+Base" target="_blank">http://kb.froglogic.com/display/KB/Squish+Knowledge+Base</a>. So now I know how to properly create tests and I can keep and execute my plan.</li>
</ul>
<p>The <strong>future</strong>:</p>
<ul>
<li>These months in the GSoC gave me a <strong>good knowledge</strong> base to keep working in the Umbrello Port as my conclusion work for college.</li>
<li>We had a suggestion  how to change the <strong>documentation support</strong> works in Umbrello: <a href="http://people.canonical.com/%7Ejriddell/tmp/umbrelloDoc.pdf" target="_blank">http://people.canonical.com/~jriddell/tmp/umbrelloDoc.pdf</a></li>
<li>And soonish we will have the <strong>Qt 5</strong>, so we will have another port project for Umbrello (but as I was adviced, I should keep with the work to port for QT 4 because the differences to Qt 5 won't be so big)</li>
<li>And there is others suggestions about how to make the Umbrello <strong>interface</strong> better and with more <strong>usability</strong>.<br />
(you can follow it in the<a href="http://uml.sourceforge.net/contact.php" target="_blank"> uml devel mail list</a>)</li>
<li>Migrate Umbrello to git.</li>
<li>Write tests using <a href="http://doc.qt.nokia.com/latest/qtestlib-manual.html" target="_blank">QtestLib</a>.</li>
</ul>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, qt, Umbrello
date: "2011-08-22T12:51:22Z"
 
published: true
status: publish
tags: desktopsummit2011, gsoc, kde-br, linkedin, umbrello
title: Desktop Summit recap and GSoC update


<p><a href="http://s196.photobucket.com/albums/aa23/holymusic55/Blessings/?action=view&amp;current=BY284Home-is-Where-Your-Heart-is-Po.jpg&amp;sort=ascending"><img class="alignright" style="padding-bottom:15px;" title="Home is where the heart is" src="/assets/images/BY284Home-is-Where-Your-Heart-is-Po.jpg" alt="Home is where the heart is" width="110" height="114" /></a> After one week being at "home" (Brazil for a while) and getting back to the normal activities (college, clean up my place, cooking for myself..), now it is time to write something about the Desktop Summit and about the last weeks of GSoC.</p>
<h2 style="margin-top:15px;">Desktop Summit</h2>
<p>It was <strong>awesome</strong> because:</p>
<p><img class=" alignleft" style="float:left;padding-right:10px;margin:10px;" title="Friends!" src="/assets/images/6067518862_5030d0b818.jpg" alt="Brazil!" width="173" height="129" /></p>
<ul>
<li>It was really nice to see <strong>new brazilian people</strong> (good friends!) attending and doing good work for KDE. You can see pictures <a title="KDE Brazil" href="http://www.flickr.com/photos/kdebr/sets/72157627363477575/" target="_blank">here</a>.</li>
<li>Really good <strong>keynotes</strong>, like the <a href="http://www.asinen.org/" target="_blank">Stuart Jarvis's</a> about "<a href="https://desktopsummit.org/program/sessions/why-are-we-here" target="_blank">Why are we here? (Community Keynote)</a>". The graphics and the quotes in the slides were very intersting (they'll be put on the website soon).</li>
</ul>
<ul>
<li>I got a Tablet in the "<a href="http://appdeveloper.intel.com/events" target="_blank">Intel AppUp Application Lab for Meego</a>"! Good <strong>workshop</strong> and good Tablet =)</li>
<li>I attended in the <strong>BoF of KDE-Promo</strong> were Stuart Jarvis, Carl Symons, Frank Karlitschek , Thomas Thym and others discussed about the KDE birthday (october!) , about the KDE People from Latin America that should try to publish more news from these countries in the dot.kde.org (that's important!) and that we need more documentation about how to get more companies "involved" with KDE. (you can follow the <a href="https://mail.kde.org/mailman/listinfo/kde-promo" target="_blank">KDE Promo e-mail list</a> to know more)</li>
<li>I attended in the <a href="http://wiki.desktopsummit.org/Workshops_%26_BoFs/2011/Kolab_Groupware" target="_blank">Kolab: The Groupware for the Free Desktop BoF</a>, where I figured out that I need to study about KDE PIM ;-)<a href="http://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Mai_Tai.jpg/220px-Mai_Tai.jpg"><img class="alignright" title="Mai Tai" src="/assets/images/220px-Mai_Tai.jpg" alt="" width="68" height="103" /></a></li>
<li>I also figured out that <a href="http://en.wikipedia.org/wiki/Mai_Tai" target="_blank">Mai Tai</a> is really dangerous - don't drink more than two or you will<br />
try to hug and say how much you love people you never saw before!</li>
<li>I met <a href="http://jriddell.org/" target="_blank">Jonathan Riddell</a>in person, my GSoC Mentor.</li>
</ul>
<p>The <strong>only bad thing</strong> about Desktop Summit 2011:</p>
<ul>
<li>The potatoes were awesome, but the most of the dishes were with pork! I don't feel like eating pork meat for the rest for the year...</li>
</ul>
<h2>GSoC</h2>
<p>The <strong>difficulties</strong>:</p>
<ul>
<li>The <strong>lack of knowledge</strong> in C++/Qt. I didn't have a lot of experience with C++/Qt when I started which made me lose some time with stupid errors, but I believe I wasn't the only one with this problem in GSoC.</li>
<li>In the beginning I was afraid about the changes that I should do in Umbrello, how to do it properly, the best way to do it.</li>
<li>I took some time to <strong>communicate</strong> properly with my mentor. I shouldn't feel so insecure about it.</li>
<li>I didn't enjoy too much to work from home.</li>
<li>Concluding: my difficulties weren't so much about the code, but more <strong>personal difficulties</strong>. I think I wrote a ambitious project which would wait more dedication from me and I didn't give all the needed dedication. So I didn't conclude the project in time.</li>
</ul>
<p>What I did to <strong>overcome</strong> it:</p>
<ul>
<li><strong>Looking for help</strong>! Mainly from KDE people that I already knew in person.</li>
<li>With this help, I had <strong>good ideas</strong> about how to proceed properly with the port:  keep the old canvas working with the new canvas to keep comparing the code, using <a href="http://www.cplusplus.com/doc/tutorial/preprocessor/" target="_blank">preprocessor directives</a> in the old code and developing the new Umbrello in a different folder in the same project.</li>
<li>After the midterm evaluation I started to <strong>skype</strong> with my mentor.</li>
</ul>
<p>The project <strong>for now</strong>:</p>
<ul>
<li>I did start to <strong>merge</strong> my code in the trunk in a new branche: <a href="http://websvn.kde.org/branches/work/umbrello-qgv-port/" target="_blank">http://websvn.kde.org/branches/work/umbrello-qgv-port/</a></li>
<li>I have the <strong>EntityWidget</strong> "working" with some bugs: <a href="http://websvn.kde.org/branches/work/soc-umbrello-2011/" target="_blank">http://websvn.kde.org/branches/work/soc-umbrello-2011/</a></li>
<li>And as I intended to do, I have <strong>the old canvas and new canvas</strong> working together as you can see in <a href="http://kders.wordpress.com/tag/gsoc-2/" target="_blank">my previous posts about the project</a>.</li>
<li>I planned to use Squish (Squish Community Edition – froglogic Squish), an software for <strong>automated GUI tests</strong>. I had some problems with this, because I was creating long tests, so the tool couldn't find all the objects from the script in the object library, but at the Desktop Summit I talked to and asked for help from <a href="http://blauzahl.livejournal.com/" target="_blank">blauzahl</a> (thanks!) and she gave some tips, like to create short and complexy tests and this useful link: <a href="http://kb.froglogic.com/display/KB/Squish+Knowledge+Base" target="_blank">http://kb.froglogic.com/display/KB/Squish+Knowledge+Base</a>. So now I know how to properly create tests and I can keep and execute my plan.</li>
</ul>
<p>The <strong>future</strong>:</p>
<ul>
<li>These months in the GSoC gave me a <strong>good knowledge</strong> base to keep working in the Umbrello Port as my conclusion work for college.</li>
<li>We had a suggestion  how to change the <strong>documentation support</strong> works in Umbrello: <a href="http://people.canonical.com/%7Ejriddell/tmp/umbrelloDoc.pdf" target="_blank">http://people.canonical.com/~jriddell/tmp/umbrelloDoc.pdf</a></li>
<li>And soonish we will have the <strong>Qt 5</strong>, so we will have another port project for Umbrello (but as I was adviced, I should keep with the work to port for QT 4 because the differences to Qt 5 won't be so big)</li>
<li>And there is others suggestions about how to make the Umbrello <strong>interface</strong> better and with more <strong>usability</strong>.<br />
(you can follow it in the<a href="http://uml.sourceforge.net/contact.php" target="_blank"> uml devel mail list</a>)</li>
<li>Migrate Umbrello to git.</li>
<li>Write tests using <a href="http://doc.qt.nokia.com/latest/qtestlib-manual.html" target="_blank">QtestLib</a>.</li>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, qt, Umbrello
date: "2011-08-22T12:51:22Z"
 
published: true
status: publish
tags: desktopsummit2011, gsoc, kde-br, linkedin, umbrello
title: Desktop Summit recap and GSoC update


<p><a href="http://s196.photobucket.com/albums/aa23/holymusic55/Blessings/?action=view&amp;current=BY284Home-is-Where-Your-Heart-is-Po.jpg&amp;sort=ascending"><img class="alignright" style="padding-bottom:15px;" title="Home is where the heart is" src="/assets/images/BY284Home-is-Where-Your-Heart-is-Po.jpg" alt="Home is where the heart is" width="110" height="114" /></a> After one week being at "home" (Brazil for a while) and getting back to the normal activities (college, clean up my place, cooking for myself..), now it is time to write something about the Desktop Summit and about the last weeks of GSoC.</p>
<h2 style="margin-top:15px;">Desktop Summit</h2>
<p>It was <strong>awesome</strong> because:</p>
<p><img class=" alignleft" style="float:left;padding-right:10px;margin:10px;" title="Friends!" src="/assets/images/6067518862_5030d0b818.jpg" alt="Brazil!" width="173" height="129" /></p>
<ul>
<li>It was really nice to see <strong>new brazilian people</strong> (good friends!) attending and doing good work for KDE. You can see pictures <a title="KDE Brazil" href="http://www.flickr.com/photos/kdebr/sets/72157627363477575/" target="_blank">here</a>.</li>
<li>Really good <strong>keynotes</strong>, like the <a href="http://www.asinen.org/" target="_blank">Stuart Jarvis's</a> about "<a href="https://desktopsummit.org/program/sessions/why-are-we-here" target="_blank">Why are we here? (Community Keynote)</a>". The graphics and the quotes in the slides were very intersting (they'll be put on the website soon).</li>
</ul>
<ul>
<li>I got a Tablet in the "<a href="http://appdeveloper.intel.com/events" target="_blank">Intel AppUp Application Lab for Meego</a>"! Good <strong>workshop</strong> and good Tablet =)</li>
<li>I attended in the <strong>BoF of KDE-Promo</strong> were Stuart Jarvis, Carl Symons, Frank Karlitschek , Thomas Thym and others discussed about the KDE birthday (october!) , about the KDE People from Latin America that should try to publish more news from these countries in the dot.kde.org (that's important!) and that we need more documentation about how to get more companies "involved" with KDE. (you can follow the <a href="https://mail.kde.org/mailman/listinfo/kde-promo" target="_blank">KDE Promo e-mail list</a> to know more)</li>
<li>I attended in the <a href="http://wiki.desktopsummit.org/Workshops_%26_BoFs/2011/Kolab_Groupware" target="_blank">Kolab: The Groupware for the Free Desktop BoF</a>, where I figured out that I need to study about KDE PIM ;-)<a href="http://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Mai_Tai.jpg/220px-Mai_Tai.jpg"><img class="alignright" title="Mai Tai" src="/assets/images/220px-Mai_Tai.jpg" alt="" width="68" height="103" /></a></li>
<li>I also figured out that <a href="http://en.wikipedia.org/wiki/Mai_Tai" target="_blank">Mai Tai</a> is really dangerous - don't drink more than two or you will<br />
try to hug and say how much you love people you never saw before!</li>
<li>I met <a href="http://jriddell.org/" target="_blank">Jonathan Riddell</a>in person, my GSoC Mentor.</li>
</ul>
<p>The <strong>only bad thing</strong> about Desktop Summit 2011:</p>
<ul>
<li>The potatoes were awesome, but the most of the dishes were with pork! I don't feel like eating pork meat for the rest for the year...</li>
</ul>
<h2>GSoC</h2>
<p>The <strong>difficulties</strong>:</p>
<ul>
<li>The <strong>lack of knowledge</strong> in C++/Qt. I didn't have a lot of experience with C++/Qt when I started which made me lose some time with stupid errors, but I believe I wasn't the only one with this problem in GSoC.</li>
<li>In the beginning I was afraid about the changes that I should do in Umbrello, how to do it properly, the best way to do it.</li>
<li>I took some time to <strong>communicate</strong> properly with my mentor. I shouldn't feel so insecure about it.</li>
<li>I didn't enjoy too much to work from home.</li>
<li>Concluding: my difficulties weren't so much about the code, but more <strong>personal difficulties</strong>. I think I wrote a ambitious project which would wait more dedication from me and I didn't give all the needed dedication. So I didn't conclude the project in time.</li>
</ul>
<p>What I did to <strong>overcome</strong> it:</p>
<ul>
<li><strong>Looking for help</strong>! Mainly from KDE people that I already knew in person.</li>
<li>With this help, I had <strong>good ideas</strong> about how to proceed properly with the port:  keep the old canvas working with the new canvas to keep comparing the code, using <a href="http://www.cplusplus.com/doc/tutorial/preprocessor/" target="_blank">preprocessor directives</a> in the old code and developing the new Umbrello in a different folder in the same project.</li>
<li>After the midterm evaluation I started to <strong>skype</strong> with my mentor.</li>
</ul>
<p>The project <strong>for now</strong>:</p>
<ul>
<li>I did start to <strong>merge</strong> my code in the trunk in a new branche: <a href="http://websvn.kde.org/branches/work/umbrello-qgv-port/" target="_blank">http://websvn.kde.org/branches/work/umbrello-qgv-port/</a></li>
<li>I have the <strong>EntityWidget</strong> "working" with some bugs: <a href="http://websvn.kde.org/branches/work/soc-umbrello-2011/" target="_blank">http://websvn.kde.org/branches/work/soc-umbrello-2011/</a></li>
<li>And as I intended to do, I have <strong>the old canvas and new canvas</strong> working together as you can see in <a href="http://kders.wordpress.com/tag/gsoc-2/" target="_blank">my previous posts about the project</a>.</li>
<li>I planned to use Squish (Squish Community Edition – froglogic Squish), an software for <strong>automated GUI tests</strong>. I had some problems with this, because I was creating long tests, so the tool couldn't find all the objects from the script in the object library, but at the Desktop Summit I talked to and asked for help from <a href="http://blauzahl.livejournal.com/" target="_blank">blauzahl</a> (thanks!) and she gave some tips, like to create short and complexy tests and this useful link: <a href="http://kb.froglogic.com/display/KB/Squish+Knowledge+Base" target="_blank">http://kb.froglogic.com/display/KB/Squish+Knowledge+Base</a>. So now I know how to properly create tests and I can keep and execute my plan.</li>
</ul>
<p>The <strong>future</strong>:</p>
<ul>
<li>These months in the GSoC gave me a <strong>good knowledge</strong> base to keep working in the Umbrello Port as my conclusion work for college.</li>
<li>We had a suggestion  how to change the <strong>documentation support</strong> works in Umbrello: <a href="http://people.canonical.com/%7Ejriddell/tmp/umbrelloDoc.pdf" target="_blank">http://people.canonical.com/~jriddell/tmp/umbrelloDoc.pdf</a></li>
<li>And soonish we will have the <strong>Qt 5</strong>, so we will have another port project for Umbrello (but as I was adviced, I should keep with the work to port for QT 4 because the differences to Qt 5 won't be so big)</li>
<li>And there is others suggestions about how to make the Umbrello <strong>interface</strong> better and with more <strong>usability</strong>.<br />
(you can follow it in the<a href="http://uml.sourceforge.net/contact.php" target="_blank"> uml devel mail list</a>)</li>
<li>Migrate Umbrello to git.</li>
<li>Write tests using <a href="http://doc.qt.nokia.com/latest/qtestlib-manual.html" target="_blank">QtestLib</a>.</li>
</ul>,-
author: Camila
categories: Archives, GSoC, KDE, planet-fosswomen, planetkde-camila, qt, Umbrello
date: "2011-08-22T12:51:22Z"
 
published: true
status: publish
tags: desktopsummit2011, gsoc, kde-br, linkedin, umbrello
title: Desktop Summit recap and GSoC update


<p><a href="http://s196.photobucket.com/albums/aa23/holymusic55/Blessings/?action=view&amp;current=BY284Home-is-Where-Your-Heart-is-Po.jpg&amp;sort=ascending"><img class="alignright" style="padding-bottom:15px;" title="Home is where the heart is" src="/assets/images/BY284Home-is-Where-Your-Heart-is-Po.jpg" alt="Home is where the heart is" width="110" height="114" /></a> After one week being at "home" (Brazil for a while) and getting back to the normal activities (college, clean up my place, cooking for myself..), now it is time to write something about the Desktop Summit and about the last weeks of GSoC.</p>
<h2 style="margin-top:15px;">Desktop Summit</h2>
<p>It was <strong>awesome</strong> because:</p>
<p><img class=" alignleft" style="float:left;padding-right:10px;margin:10px;" title="Friends!" src="/assets/images/6067518862_5030d0b818.jpg" alt="Brazil!" width="173" height="129" /></p>
<ul>
<li>It was really nice to see <strong>new brazilian people</strong> (good friends!) attending and doing good work for KDE. You can see pictures <a title="KDE Brazil" href="http://www.flickr.com/photos/kdebr/sets/72157627363477575/" target="_blank">here</a>.</li>
<li>Really good <strong>keynotes</strong>, like the <a href="http://www.asinen.org/" target="_blank">Stuart Jarvis's</a> about "<a href="https://desktopsummit.org/program/sessions/why-are-we-here" target="_blank">Why are we here? (Community Keynote)</a>". The graphics and the quotes in the slides were very intersting (they'll be put on the website soon).</li>
</ul>
<ul>
<li>I got a Tablet in the "<a href="http://appdeveloper.intel.com/events" target="_blank">Intel AppUp Application Lab for Meego</a>"! Good <strong>workshop</strong> and good Tablet =)</li>
<li>I attended in the <strong>BoF of KDE-Promo</strong> were Stuart Jarvis, Carl Symons, Frank Karlitschek , Thomas Thym and others discussed about the KDE birthday (october!) , about the KDE People from Latin America that should try to publish more news from these countries in the dot.kde.org (that's important!) and that we need more documentation about how to get more companies "involved" with KDE. (you can follow the <a href="https://mail.kde.org/mailman/listinfo/kde-promo" target="_blank">KDE Promo e-mail list</a> to know more)</li>
<li>I attended in the <a href="http://wiki.desktopsummit.org/Workshops_%26_BoFs/2011/Kolab_Groupware" target="_blank">Kolab: The Groupware for the Free Desktop BoF</a>, where I figured out that I need to study about KDE PIM ;-)<a href="http://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Mai_Tai.jpg/220px-Mai_Tai.jpg"><img class="alignright" title="Mai Tai" src="/assets/images/220px-Mai_Tai.jpg" alt="" width="68" height="103" /></a></li>
<li>I also figured out that <a href="http://en.wikipedia.org/wiki/Mai_Tai" target="_blank">Mai Tai</a> is really dangerous - don't drink more than two or you will<br />
try to hug and say how much you love people you never saw before!</li>
<li>I met <a href="http://jriddell.org/" target="_blank">Jonathan Riddell</a>in person, my GSoC Mentor.</li>
</ul>
<p>The <strong>only bad thing</strong> about Desktop Summit 2011:</p>
<ul>
<li>The potatoes were awesome, but the most of the dishes were with pork! I don't feel like eating pork meat for the rest for the year...</li>
</ul>
<h2>GSoC</h2>
<p>The <strong>difficulties</strong>:</p>
<ul>
<li>The <strong>lack of knowledge</strong> in C++/Qt. I didn't have a lot of experience with C++/Qt when I started which made me lose some time with stupid errors, but I believe I wasn't the only one with this problem in GSoC.</li>
<li>In the beginning I was afraid about the changes that I should do in Umbrello, how to do it properly, the best way to do it.</li>
<li>I took some time to <strong>communicate</strong> properly with my mentor. I shouldn't feel so insecure about it.</li>
<li>I didn't enjoy too much to work from home.</li>
<li>Concluding: my difficulties weren't so much about the code, but more <strong>personal difficulties</strong>. I think I wrote a ambitious project which would wait more dedication from me and I didn't give all the needed dedication. So I didn't conclude the project in time.</li>
</ul>
<p>What I did to <strong>overcome</strong> it:</p>
<ul>
<li><strong>Looking for help</strong>! Mainly from KDE people that I already knew in person.</li>
<li>With this help, I had <strong>good ideas</strong> about how to proceed properly with the port:  keep the old canvas working with the new canvas to keep comparing the code, using <a href="http://www.cplusplus.com/doc/tutorial/preprocessor/" target="_blank">preprocessor directives</a> in the old code and developing the new Umbrello in a different folder in the same project.</li>
<li>After the midterm evaluation I started to <strong>skype</strong> with my mentor.</li>
</ul>
<p>The project <strong>for now</strong>:</p>
<ul>
<li>I did start to <strong>merge</strong> my code in the trunk in a new branche: <a href="http://websvn.kde.org/branches/work/umbrello-qgv-port/" target="_blank">http://websvn.kde.org/branches/work/umbrello-qgv-port/</a></li>
<li>I have the <strong>EntityWidget</strong> "working" with some bugs: <a href="http://websvn.kde.org/branches/work/soc-umbrello-2011/" target="_blank">http://websvn.kde.org/branches/work/soc-umbrello-2011/</a></li>
<li>And as I intended to do, I have <strong>the old canvas and new canvas</strong> working together as you can see in <a href="http://kders.wordpress.com/tag/gsoc-2/" target="_blank">my previous posts about the project</a>.</li>
<li>I planned to use Squish (Squish Community Edition – froglogic Squish), an software for <strong>automated GUI tests</strong>. I had some problems with this, because I was creating long tests, so the tool couldn't find all the objects from the script in the object library, but at the Desktop Summit I talked to and asked for help from <a href="http://blauzahl.livejournal.com/" target="_blank">blauzahl</a> (thanks!) and she gave some tips, like to create short and complexy tests and this useful link: <a href="http://kb.froglogic.com/display/KB/Squish+Knowledge+Base" target="_blank">http://kb.froglogic.com/display/KB/Squish+Knowledge+Base</a>. So now I know how to properly create tests and I can keep and execute my plan.</li>
</ul>
<p>The <strong>future</strong>:</p>
<ul>
<li>These months in the GSoC gave me a <strong>good knowledge</strong> base to keep working in the Umbrello Port as my conclusion work for college.</li>
<li>We had a suggestion  how to change the <strong>documentation support</strong> works in Umbrello: <a href="http://people.canonical.com/%7Ejriddell/tmp/umbrelloDoc.pdf" target="_blank">http://people.canonical.com/~jriddell/tmp/umbrelloDoc.pdf</a></li>
<li>And soonish we will have the <strong>Qt 5</strong>, so we will have another port project for Umbrello (but as I was adviced, I should keep with the work to port for QT 4 because the differences to Qt 5 won't be so big)</li>
<li>And there is others suggestions about how to make the Umbrello <strong>interface</strong> better and with more <strong>usability</strong>.<br />
(you can follow it in the<a href="http://uml.sourceforge.net/contact.php" target="_blank"> uml devel mail list</a>)</li>
<li>Migrate Umbrello to git.</li>
<li>Write tests using <a href="http://doc.qt.nokia.com/latest/qtestlib-manual.html" target="_blank">QtestLib</a>.</li>
</ul>
