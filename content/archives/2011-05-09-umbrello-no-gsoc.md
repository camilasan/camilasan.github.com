
author: Camila
categories: Archives, GSoC, planetkde-pt-camila, Umbrello
date: "2011-05-09T07:19:09Z"
 
published: true
status: publish
tags: gsoc, kde, umbrello
title: Umbrello no GSoC


<h1>A primeira semana de trabalho planejada:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (Eu conversei um pouco com os meus colegas de grupo do GSoC )<br />
* Review Plan with Mentor. (Conversei com o Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>...e se acostumar a trabalhar de casa :)</p>
<h2>Portando o Umbrello:</h2>
<p>A melhor maneira de trabalhar encontrada para realizar as alterações por partes foi manter as classes antigas e criar as novas classes em conjunto. Assim, incluir as chamadas para os novos métodos nos arquivos antigos mantendo o funcionamento dos dois e com isso testando o funcionamento dos novos métodos.</p>
<p>O resultado no momento é o Umbrello antigo funcionando com uma janela nova mostrando o "novo canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>Nesse "view" já com QGraphicsView é que eu vou testar as minhas novas classes.</p>
<h2>Usando o Squish para gravar testes:</h2>
<p>Para tentar tomar a melhor decisão com respeito a como proceder para o port, que partes do codigo reaproveitar, eu fiz alguns diagramas de classe (apenas uns rascunhos), com as principais classes, as que eu devo trabalhar.</p>
<p>Com isso, eu achei que seria interessante desenhar o diagrama no Umbrello, e gravar alguns passos no Squish (eu to usando o Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - disponível apenas para testar softwares do KDE, voce pode pedir pelo e-mail: squishkde@froglogic.com) . A vantagem foi pegar alguma prática com o Software (também descobrir e reportar alguns bugs :/)</p>
<p>E é muito facil de gravar testes com o Squish, você pode automatizar os testes ou escrever os scripts na mão. O que é cansativo é que a medida que você grava os testes, o sistema armazena uma tabela com os objetos da tua aplicação. Mas se o o bjeto não estiver nessa tabela ainda, o teste pára e é necessário incluir o objeto ou editando a tabela no braço, ou executando a aplicação no modo Spy ou ainda simplesmente gravar testes 'dummies' onde você deve usar os objetos que você precisa no teste. Você pode tirar as suas próprias conclusões conferindo o link: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Alguns links interessantes:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Próximas semanas:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>O meu plano de trabalho completo você pode ver aqui: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>,-
author: Camila
categories: Archives, GSoC, planetkde-pt-camila, Umbrello
date: "2011-05-09T07:19:09Z"
 
published: true
status: publish
tags: gsoc, kde, umbrello
title: Umbrello no GSoC


<h1>A primeira semana de trabalho planejada:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (Eu conversei um pouco com os meus colegas de grupo do GSoC )<br />
* Review Plan with Mentor. (Conversei com o Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>...e se acostumar a trabalhar de casa :)</p>
<h2>Portando o Umbrello:</h2>
<p>A melhor maneira de trabalhar encontrada para realizar as alterações por partes foi manter as classes antigas e criar as novas classes em conjunto. Assim, incluir as chamadas para os novos métodos nos arquivos antigos mantendo o funcionamento dos dois e com isso testando o funcionamento dos novos métodos.</p>
<p>O resultado no momento é o Umbrello antigo funcionando com uma janela nova mostrando o "novo canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>Nesse "view" já com QGraphicsView é que eu vou testar as minhas novas classes.</p>
<h2>Usando o Squish para gravar testes:</h2>
<p>Para tentar tomar a melhor decisão com respeito a como proceder para o port, que partes do codigo reaproveitar, eu fiz alguns diagramas de classe (apenas uns rascunhos), com as principais classes, as que eu devo trabalhar.</p>
<p>Com isso, eu achei que seria interessante desenhar o diagrama no Umbrello, e gravar alguns passos no Squish (eu to usando o Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - disponível apenas para testar softwares do KDE, voce pode pedir pelo e-mail: squishkde@froglogic.com) . A vantagem foi pegar alguma prática com o Software (também descobrir e reportar alguns bugs :/)</p>
<p>E é muito facil de gravar testes com o Squish, você pode automatizar os testes ou escrever os scripts na mão. O que é cansativo é que a medida que você grava os testes, o sistema armazena uma tabela com os objetos da tua aplicação. Mas se o o bjeto não estiver nessa tabela ainda, o teste pára e é necessário incluir o objeto ou editando a tabela no braço, ou executando a aplicação no modo Spy ou ainda simplesmente gravar testes 'dummies' onde você deve usar os objetos que você precisa no teste. Você pode tirar as suas próprias conclusões conferindo o link: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Alguns links interessantes:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Próximas semanas:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>O meu plano de trabalho completo você pode ver aqui: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>
<p>Acredito que, assim como a maioria dos estudantes, a minha expectativa com o GSoC é aprender MUITO e realizar um BOM trabalho. E mesmo depois desse período continuar contribuindo para a comunidade :)</p>,-
author: Camila
categories: Archives, GSoC, planetkde-pt-camila, Umbrello
date: "2011-05-09T07:19:09Z"
 
published: true
status: publish
tags: gsoc, kde, umbrello
title: Umbrello no GSoC


<h1>A primeira semana de trabalho planejada:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (Eu conversei um pouco com os meus colegas de grupo do GSoC )<br />
* Review Plan with Mentor. (Conversei com o Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>...e se acostumar a trabalhar de casa :)</p>
<h2>Portando o Umbrello:</h2>
<p>A melhor maneira de trabalhar encontrada para realizar as alterações por partes foi manter as classes antigas e criar as novas classes em conjunto. Assim, incluir as chamadas para os novos métodos nos arquivos antigos mantendo o funcionamento dos dois e com isso testando o funcionamento dos novos métodos.</p>
<p>O resultado no momento é o Umbrello antigo funcionando com uma janela nova mostrando o "novo canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>Nesse "view" já com QGraphicsView é que eu vou testar as minhas novas classes.</p>
<h2>Usando o Squish para gravar testes:</h2>
<p>Para tentar tomar a melhor decisão com respeito a como proceder para o port, que partes do codigo reaproveitar, eu fiz alguns diagramas de classe (apenas uns rascunhos), com as principais classes, as que eu devo trabalhar.</p>
<p>Com isso, eu achei que seria interessante desenhar o diagrama no Umbrello, e gravar alguns passos no Squish (eu to usando o Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - disponível apenas para testar softwares do KDE, voce pode pedir pelo e-mail: squishkde@froglogic.com) . A vantagem foi pegar alguma prática com o Software (também descobrir e reportar alguns bugs :/)</p>
<p>E é muito facil de gravar testes com o Squish, você pode automatizar os testes ou escrever os scripts na mão. O que é cansativo é que a medida que você grava os testes, o sistema armazena uma tabela com os objetos da tua aplicação. Mas se o o bjeto não estiver nessa tabela ainda, o teste pára e é necessário incluir o objeto ou editando a tabela no braço, ou executando a aplicação no modo Spy ou ainda simplesmente gravar testes 'dummies' onde você deve usar os objetos que você precisa no teste. Você pode tirar as suas próprias conclusões conferindo o link: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Alguns links interessantes:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Próximas semanas:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>O meu plano de trabalho completo você pode ver aqui: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>,-
author: Camila
categories: Archives, GSoC, planetkde-pt-camila, Umbrello
date: "2011-05-09T07:19:09Z"
 
published: true
status: publish
tags: gsoc, kde, umbrello
title: Umbrello no GSoC


<h1>A primeira semana de trabalho planejada:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (Eu conversei um pouco com os meus colegas de grupo do GSoC )<br />
* Review Plan with Mentor. (Conversei com o Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>...e se acostumar a trabalhar de casa :)</p>
<h2>Portando o Umbrello:</h2>
<p>A melhor maneira de trabalhar encontrada para realizar as alterações por partes foi manter as classes antigas e criar as novas classes em conjunto. Assim, incluir as chamadas para os novos métodos nos arquivos antigos mantendo o funcionamento dos dois e com isso testando o funcionamento dos novos métodos.</p>
<p>O resultado no momento é o Umbrello antigo funcionando com uma janela nova mostrando o "novo canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>Nesse "view" já com QGraphicsView é que eu vou testar as minhas novas classes.</p>
<h2>Usando o Squish para gravar testes:</h2>
<p>Para tentar tomar a melhor decisão com respeito a como proceder para o port, que partes do codigo reaproveitar, eu fiz alguns diagramas de classe (apenas uns rascunhos), com as principais classes, as que eu devo trabalhar.</p>
<p>Com isso, eu achei que seria interessante desenhar o diagrama no Umbrello, e gravar alguns passos no Squish (eu to usando o Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - disponível apenas para testar softwares do KDE, voce pode pedir pelo e-mail: squishkde@froglogic.com) . A vantagem foi pegar alguma prática com o Software (também descobrir e reportar alguns bugs :/)</p>
<p>E é muito facil de gravar testes com o Squish, você pode automatizar os testes ou escrever os scripts na mão. O que é cansativo é que a medida que você grava os testes, o sistema armazena uma tabela com os objetos da tua aplicação. Mas se o o bjeto não estiver nessa tabela ainda, o teste pára e é necessário incluir o objeto ou editando a tabela no braço, ou executando a aplicação no modo Spy ou ainda simplesmente gravar testes 'dummies' onde você deve usar os objetos que você precisa no teste. Você pode tirar as suas próprias conclusões conferindo o link: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Alguns links interessantes:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Próximas semanas:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>O meu plano de trabalho completo você pode ver aqui: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>,-
author: Camila
categories: Archives, GSoC, planetkde-pt-camila, Umbrello
date: "2011-05-09T07:19:09Z"
 
published: true
status: publish
tags: gsoc, kde, umbrello
title: Umbrello no GSoC


<h1>A primeira semana de trabalho planejada:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (Eu conversei um pouco com os meus colegas de grupo do GSoC )<br />
* Review Plan with Mentor. (Conversei com o Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>...e se acostumar a trabalhar de casa :)</p>
<h2>Portando o Umbrello:</h2>
<p>A melhor maneira de trabalhar encontrada para realizar as alterações por partes foi manter as classes antigas e criar as novas classes em conjunto. Assim, incluir as chamadas para os novos métodos nos arquivos antigos mantendo o funcionamento dos dois e com isso testando o funcionamento dos novos métodos.</p>
<p>O resultado no momento é o Umbrello antigo funcionando com uma janela nova mostrando o "novo canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>Nesse "view" já com QGraphicsView é que eu vou testar as minhas novas classes.</p>
<h2>Usando o Squish para gravar testes:</h2>
<p>Para tentar tomar a melhor decisão com respeito a como proceder para o port, que partes do codigo reaproveitar, eu fiz alguns diagramas de classe (apenas uns rascunhos), com as principais classes, as que eu devo trabalhar.</p>
<p>Com isso, eu achei que seria interessante desenhar o diagrama no Umbrello, e gravar alguns passos no Squish (eu to usando o Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - disponível apenas para testar softwares do KDE, voce pode pedir pelo e-mail: squishkde@froglogic.com) . A vantagem foi pegar alguma prática com o Software (também descobrir e reportar alguns bugs :/)</p>
<p>E é muito facil de gravar testes com o Squish, você pode automatizar os testes ou escrever os scripts na mão. O que é cansativo é que a medida que você grava os testes, o sistema armazena uma tabela com os objetos da tua aplicação. Mas se o o bjeto não estiver nessa tabela ainda, o teste pára e é necessário incluir o objeto ou editando a tabela no braço, ou executando a aplicação no modo Spy ou ainda simplesmente gravar testes 'dummies' onde você deve usar os objetos que você precisa no teste. Você pode tirar as suas próprias conclusões conferindo o link: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Alguns links interessantes:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Próximas semanas:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>O meu plano de trabalho completo você pode ver aqui: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>
<p>Acredito que, assim como a maioria dos estudantes, a minha expectativa com o GSoC é aprender MUITO e realizar um BOM trabalho. E mesmo depois desse período continuar contribuindo para a comunidade :)</p>,-
author: Camila
categories: Archives, GSoC, planetkde-pt-camila, Umbrello
date: "2011-05-09T07:19:09Z"
 
published: true
status: publish
tags: gsoc, kde, umbrello
title: Umbrello no GSoC


<h1>A primeira semana de trabalho planejada:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (Eu conversei um pouco com os meus colegas de grupo do GSoC )<br />
* Review Plan with Mentor. (Conversei com o Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>...e se acostumar a trabalhar de casa :)</p>
<h2>Portando o Umbrello:</h2>
<p>A melhor maneira de trabalhar encontrada para realizar as alterações por partes foi manter as classes antigas e criar as novas classes em conjunto. Assim, incluir as chamadas para os novos métodos nos arquivos antigos mantendo o funcionamento dos dois e com isso testando o funcionamento dos novos métodos.</p>
<p>O resultado no momento é o Umbrello antigo funcionando com uma janela nova mostrando o "novo canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>Nesse "view" já com QGraphicsView é que eu vou testar as minhas novas classes.</p>
<h2>Usando o Squish para gravar testes:</h2>
<p>Para tentar tomar a melhor decisão com respeito a como proceder para o port, que partes do codigo reaproveitar, eu fiz alguns diagramas de classe (apenas uns rascunhos), com as principais classes, as que eu devo trabalhar.</p>
<p>Com isso, eu achei que seria interessante desenhar o diagrama no Umbrello, e gravar alguns passos no Squish (eu to usando o Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - disponível apenas para testar softwares do KDE, voce pode pedir pelo e-mail: squishkde@froglogic.com) . A vantagem foi pegar alguma prática com o Software (também descobrir e reportar alguns bugs :/)</p>
<p>E é muito facil de gravar testes com o Squish, você pode automatizar os testes ou escrever os scripts na mão. O que é cansativo é que a medida que você grava os testes, o sistema armazena uma tabela com os objetos da tua aplicação. Mas se o o bjeto não estiver nessa tabela ainda, o teste pára e é necessário incluir o objeto ou editando a tabela no braço, ou executando a aplicação no modo Spy ou ainda simplesmente gravar testes 'dummies' onde você deve usar os objetos que você precisa no teste. Você pode tirar as suas próprias conclusões conferindo o link: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Alguns links interessantes:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Próximas semanas:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>O meu plano de trabalho completo você pode ver aqui: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>
<p>Acredito que, assim como a maioria dos estudantes, a minha expectativa com o GSoC é aprender MUITO e realizar um BOM trabalho. E mesmo depois desse período continuar contribuindo para a comunidade :)</p>,-
author: Camila
categories: Archives, GSoC, planetkde-pt-camila, Umbrello
date: "2011-05-09T07:19:09Z"
 
published: true
status: publish
tags: gsoc, kde, umbrello
title: Umbrello no GSoC


<h1>A primeira semana de trabalho planejada:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (Eu conversei um pouco com os meus colegas de grupo do GSoC )<br />
* Review Plan with Mentor. (Conversei com o Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>...e se acostumar a trabalhar de casa :)</p>
<h2>Portando o Umbrello:</h2>
<p>A melhor maneira de trabalhar encontrada para realizar as alterações por partes foi manter as classes antigas e criar as novas classes em conjunto. Assim, incluir as chamadas para os novos métodos nos arquivos antigos mantendo o funcionamento dos dois e com isso testando o funcionamento dos novos métodos.</p>
<p>O resultado no momento é o Umbrello antigo funcionando com uma janela nova mostrando o "novo canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>Nesse "view" já com QGraphicsView é que eu vou testar as minhas novas classes.</p>
<h2>Usando o Squish para gravar testes:</h2>
<p>Para tentar tomar a melhor decisão com respeito a como proceder para o port, que partes do codigo reaproveitar, eu fiz alguns diagramas de classe (apenas uns rascunhos), com as principais classes, as que eu devo trabalhar.</p>
<p>Com isso, eu achei que seria interessante desenhar o diagrama no Umbrello, e gravar alguns passos no Squish (eu to usando o Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - disponível apenas para testar softwares do KDE, voce pode pedir pelo e-mail: squishkde@froglogic.com) . A vantagem foi pegar alguma prática com o Software (também descobrir e reportar alguns bugs :/)</p>
<p>E é muito facil de gravar testes com o Squish, você pode automatizar os testes ou escrever os scripts na mão. O que é cansativo é que a medida que você grava os testes, o sistema armazena uma tabela com os objetos da tua aplicação. Mas se o o bjeto não estiver nessa tabela ainda, o teste pára e é necessário incluir o objeto ou editando a tabela no braço, ou executando a aplicação no modo Spy ou ainda simplesmente gravar testes 'dummies' onde você deve usar os objetos que você precisa no teste. Você pode tirar as suas próprias conclusões conferindo o link: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Alguns links interessantes:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Próximas semanas:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>O meu plano de trabalho completo você pode ver aqui: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>,-
author: Camila
categories: Archives, GSoC, planetkde-pt-camila, Umbrello
date: "2011-05-09T07:19:09Z"
 
published: true
status: publish
tags: gsoc, kde, umbrello
title: Umbrello no GSoC


<h1>A primeira semana de trabalho planejada:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (Eu conversei um pouco com os meus colegas de grupo do GSoC )<br />
* Review Plan with Mentor. (Conversei com o Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>...e se acostumar a trabalhar de casa :)</p>
<h2>Portando o Umbrello:</h2>
<p>A melhor maneira de trabalhar encontrada para realizar as alterações por partes foi manter as classes antigas e criar as novas classes em conjunto. Assim, incluir as chamadas para os novos métodos nos arquivos antigos mantendo o funcionamento dos dois e com isso testando o funcionamento dos novos métodos.</p>
<p>O resultado no momento é o Umbrello antigo funcionando com uma janela nova mostrando o "novo canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>Nesse "view" já com QGraphicsView é que eu vou testar as minhas novas classes.</p>
<h2>Usando o Squish para gravar testes:</h2>
<p>Para tentar tomar a melhor decisão com respeito a como proceder para o port, que partes do codigo reaproveitar, eu fiz alguns diagramas de classe (apenas uns rascunhos), com as principais classes, as que eu devo trabalhar.</p>
<p>Com isso, eu achei que seria interessante desenhar o diagrama no Umbrello, e gravar alguns passos no Squish (eu to usando o Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - disponível apenas para testar softwares do KDE, voce pode pedir pelo e-mail: squishkde@froglogic.com) . A vantagem foi pegar alguma prática com o Software (também descobrir e reportar alguns bugs :/)</p>
<p>E é muito facil de gravar testes com o Squish, você pode automatizar os testes ou escrever os scripts na mão. O que é cansativo é que a medida que você grava os testes, o sistema armazena uma tabela com os objetos da tua aplicação. Mas se o o bjeto não estiver nessa tabela ainda, o teste pára e é necessário incluir o objeto ou editando a tabela no braço, ou executando a aplicação no modo Spy ou ainda simplesmente gravar testes 'dummies' onde você deve usar os objetos que você precisa no teste. Você pode tirar as suas próprias conclusões conferindo o link: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Alguns links interessantes:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Próximas semanas:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>O meu plano de trabalho completo você pode ver aqui: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>
<p>Acredito que, assim como a maioria dos estudantes, a minha expectativa com o GSoC é aprender MUITO e realizar um BOM trabalho. E mesmo depois desse período continuar contribuindo para a comunidade :)</p>,-
author: Camila
categories: Archives, GSoC, planetkde-pt-camila, Umbrello
date: "2011-05-09T07:19:09Z"
 
published: true
status: publish
tags: gsoc, kde, umbrello
title: Umbrello no GSoC


<h1>A primeira semana de trabalho planejada:</h1>
<p>25 April - 08 May</p>
<p>* Community Bonding Period. (Eu conversei um pouco com os meus colegas de grupo do GSoC )<br />
* Review Plan with Mentor. (Conversei com o Jonathan)<br />
* Get instructions for the work and get started!</p>
<p>...e se acostumar a trabalhar de casa :)</p>
<h2>Portando o Umbrello:</h2>
<p>A melhor maneira de trabalhar encontrada para realizar as alterações por partes foi manter as classes antigas e criar as novas classes em conjunto. Assim, incluir as chamadas para os novos métodos nos arquivos antigos mantendo o funcionamento dos dois e com isso testando o funcionamento dos novos métodos.</p>
<p>O resultado no momento é o Umbrello antigo funcionando com uma janela nova mostrando o "novo canvas":</p>
<p><img src="/assets/images/primeiro-sprint.png" alt="" /></p>
<p>Nesse "view" já com QGraphicsView é que eu vou testar as minhas novas classes.</p>
<h2>Usando o Squish para gravar testes:</h2>
<p>Para tentar tomar a melhor decisão com respeito a como proceder para o port, que partes do codigo reaproveitar, eu fiz alguns diagramas de classe (apenas uns rascunhos), com as principais classes, as que eu devo trabalhar.</p>
<p>Com isso, eu achei que seria interessante desenhar o diagrama no Umbrello, e gravar alguns passos no Squish (eu to usando o Squish Community Edition - froglogic Squish IDE 4.1.0-SNAPSHOT - disponível apenas para testar softwares do KDE, voce pode pedir pelo e-mail: squishkde@froglogic.com) . A vantagem foi pegar alguma prática com o Software (também descobrir e reportar alguns bugs :/)</p>
<p>E é muito facil de gravar testes com o Squish, você pode automatizar os testes ou escrever os scripts na mão. O que é cansativo é que a medida que você grava os testes, o sistema armazena uma tabela com os objetos da tua aplicação. Mas se o o bjeto não estiver nessa tabela ainda, o teste pára e é necessário incluir o objeto ou editando a tabela no braço, ou executando a aplicação no modo Spy ou ainda simplesmente gravar testes 'dummies' onde você deve usar os objetos que você precisa no teste. Você pode tirar as suas próprias conclusões conferindo o link: <a href="http://doc.froglogic.com/squish/latest/all/" target="_blank">http://doc.froglogic.com/squish/latest/all/</a></p>
<h2>Alguns links interessantes:</h2>
<p>QObject x QGraphicsObject:<br />
. <a href="http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit" target="_blank">http://stackoverflow.com/questions/4922801/adding-signals-slots-qobject-to-qgraphicsitem-performance-hit</a><br />
. <a href="http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem" target="_blank">http://stackoverflow.com/questions/2292072/penalty-of-using-qgraphicsobject-vs-qgraphicsitem</a></p>
<p>Qt GraphicsView in depth:<br />
. <a href="http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth" target="_blank">http://qt.nokia.com/developer/learning/online/talks/developerdays2010/tech-talks/qt-graphics-view-in-depth </a></p>
<p>QTestLib:<br />
. <a href="http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib" target="_blank">http://doc.qt.nokia.com/4.7/qtestlib-manual.html#qtestlib<br />
</a>. <a href="http://qt.gitorious.org/qt-labs/qtestlib-tools" target="_blank">http://qt.gitorious.org/qt-labs/qtestlib-tools</a></p>
<h2>Próximas semanas:</h2>
<p>Sprint 1: 09 May - 22 May</p>
<p>* UMLViewCanvas, LinePath, Circle, SubsetSymbol, SeqLineWidget, UMLView (Classes that implement the view for the diagrams, graphical representation of sequence lines and that represent diagrams)</p>
<p>O meu plano de trabalho completo você pode ver aqui: <a href="http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/camilasan/1" target="_blank">Umbrello UML Modeller QGraphicsView Port</a></p>
<p>Acredito que, assim como a maioria dos estudantes, a minha expectativa com o GSoC é aprender MUITO e realizar um BOM trabalho. E mesmo depois desse período continuar contribuindo para a comunidade :)</p>
