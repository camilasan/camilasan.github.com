author: Camila
categories: Archives, Personal/Pessoal, poo, Programming
date: 2010-04-20 13:31:26
tags:  poo, Programming
title: Sobrecarga != Sobrescrita

<p>Em um rápido lapso de raciocínio você também chegou a pensar que sobecarga é a mesma coisa que sobrescrita?<br />
Calma, que o @tumaix te explica:</p>
<p>"Sobrecarga é uma coisa, Sobrescrita é outra.</p>
<p>Sobrecarga:<br />
Métodos na mesma classe, com nome igual e argumentos diferentes.</p>
<p>ex., imagina que você tem 4 classes, 'Jogador', 'Mesa', 'Baralho' e<br />
'Carta', aonde o Baralho tem que dar cartas a mesa e Jogador. em<br />
Linguagens que não tem sobrecarga, você recisa fazer algo como</p>
<p>Class BaralhoSemSobrecarga{<br />
void daCartasJogador(Jogador j);<br />
void daCartasMesa(Mesa m);<br />
};</p>
<p>só a assinatura. Mas poxa, a 'Razão de ser' de ambos os métodos é um<br />
só, que é dar cartas. dai veio a idéia de sobrecarga, que é fazer um<br />
jeito dos métodos existirem com mesmo nome, mas funcionarem de forma<br />
diferente:</p>
<p>Class BaralhoComSobrecarga{<br />
void daCartas(Jogador j);<br />
void daCartas(Mesa m);<br />
}</p>
<p>como os tipos utilizados dentro do método são diferentes, o compilador<br />
constroi o método para ser invocado pelo nome + tipo de parametro<br />
passado ( descoberto pelo comando typeid() ), e só então chama o<br />
método correto. isso é bem bom pra manter a coerência do programa.</p>
<p>Já sobrescrita é quando você cria um método em uma classe:<br />
class Gente{<br />
virtual void falar(){ std::cout &lt;&lt; "Eu sou gente" };<br />
}<br />
class Pai : public Gente{<br />
void falar(){ std::cout &lt;&lt; "Oi, eu sou o pai"; }<br />
}<br />
class Filho : public Gente{<br />
void falar(){std::cout &lt;&lt; "Oi eu sou o filho"; }<br />
}</p>
<p>temos 3 classes, bem pequenas, só pra comparar.</p>
<p>Gente *a = new Gente();<br />
Gente *b = new Pai();<br />
Gente *c = new Filho();</p>
<p>eu criei 3 objetos do tipo 'Gente', só que dois dele são subclasses.<br />
isso significa que eu posso fazer<br />
a-&gt;falar() e vai sair "Eu sou gente";<br />
b-&gt; falar() e vai sair "Eu sou o pai";<br />
c-&gt; falar() e vai sair "Eu sou o filho".</p>
<p>porque os métodos das classes filho sobrescreveram a classe pai.<br />
isso entretanto, só ocorre quando o método é virtual ( no c++ ) e no<br />
java tem Override.</p>
<p>só que, po, eu tou numa classe 'Gente', como é que ele chama o método<br />
da classe 'Pai' ou 'Filho'? o new não tem nada haver com isso, já que<br />
depois que eu dou o new, caio em um ponteiro de 'Gente' e gente é<br />
sempre gente.</p>
<p>só que como marquei o método como virtual, ele consegue descobrir qual<br />
o tipo de classe que está associada a memória por uma coisa chamada<br />
vTable ( Virtual Method Table ), que é uma tabela de variação de<br />
métodos que é construida pelo compilador no momento que o programa<br />
está sendo gerado, e essa tabela guarda as informações de classe e<br />
parametros para ser disparado quando usada. ( se usar o comando -fdump<br />
do g++ você consegue ver a tabela gerada ), aqui num exemplo simples<br />
deu o seguinte:</p>
<p>d:<br />
+0: pointer to virtual method table of D (for B1)<br />
+4: value of int_in_b1<br />
+8: pointer to virtual method table of D (for B2)<br />
+12: value of int_in_b2<br />
+16: value of int_in_d</p>
<p>isso me diz que o 0 e o 12 (binários: 000000, 001100 ) são ponteiros<br />
para métodos que estão na verdade em outra classe, e acessando esses<br />
ponteiros, que indicam a posição da memória de execução ( não de dados<br />
) ele consegue saber o código que será executado.</p>
<p>e Isso é sobrescrita =)"</p>
<p>e eu:</p>
<p>"<span style="font-family:trebuchet ms, sans-serif;">deixa ver se eu entendi:<br />
em  sobrecarga temos 2 metodos com o mesmo nome que pertencem a mesma classe  e com funções diferentes (certo?)"<br />
<em>- sim!</em><br />
"em sobrescrita temos metodos  com o mesmo nome que pertencem a classes diferentes e que sobrescrevem o  método da classe pai com o mesmo nome. se o metdodo da classe filha nao  é virtual, qdo chamado ele vai executar o metodo da classe pai?</span>"<br />
<em>- sim!</em></p>
<p>Valeu @tumaix.</p>,-
author: Camila
categories: Archives, Personal/Pessoal, poo, Programming
date: "2010-04-20T13:31:26Z"

published: true
status: publish
tags: poo, Programming
title: Sobrecarga != Sobrescrita


<p>Em um rápido lapso de raciocínio você também chegou a pensar que sobecarga é a mesma coisa que sobrescrita?<br />
Calma, que o @tumaix te explica:</p>
<p>"Sobrecarga é uma coisa, Sobrescrita é outra.</p>
<p>Sobrecarga:<br />
Métodos na mesma classe, com nome igual e argumentos diferentes.</p>
<p>ex., imagina que você tem 4 classes, 'Jogador', 'Mesa', 'Baralho' e<br />
'Carta', aonde o Baralho tem que dar cartas a mesa e Jogador. em<br />
Linguagens que não tem sobrecarga, você recisa fazer algo como</p>
<p>Class BaralhoSemSobrecarga{<br />
void daCartasJogador(Jogador j);<br />
void daCartasMesa(Mesa m);<br />
};</p>
<p>só a assinatura. Mas poxa, a 'Razão de ser' de ambos os métodos é um<br />
só, que é dar cartas. dai veio a idéia de sobrecarga, que é fazer um<br />
jeito dos métodos existirem com mesmo nome, mas funcionarem de forma<br />
diferente:</p>
<p>Class BaralhoComSobrecarga{<br />
void daCartas(Jogador j);<br />
void daCartas(Mesa m);<br />
}</p>
<p>como os tipos utilizados dentro do método são diferentes, o compilador<br />
constroi o método para ser invocado pelo nome + tipo de parametro<br />
passado ( descoberto pelo comando typeid() ), e só então chama o<br />
método correto. isso é bem bom pra manter a coerência do programa.</p>
<p>Já sobrescrita é quando você cria um método em uma classe:<br />
class Gente{<br />
virtual void falar(){ std::cout &lt;&lt; "Eu sou gente" };<br />
}<br />
class Pai : public Gente{<br />
void falar(){ std::cout &lt;&lt; "Oi, eu sou o pai"; }<br />
}<br />
class Filho : public Gente{<br />
void falar(){std::cout &lt;&lt; "Oi eu sou o filho"; }<br />
}</p>
<p>temos 3 classes, bem pequenas, só pra comparar.</p>
<p>Gente *a = new Gente();<br />
Gente *b = new Pai();<br />
Gente *c = new Filho();</p>
<p>eu criei 3 objetos do tipo 'Gente', só que dois dele são subclasses.<br />
isso significa que eu posso fazer<br />
a-&gt;falar() e vai sair "Eu sou gente";<br />
b-&gt; falar() e vai sair "Eu sou o pai";<br />
c-&gt; falar() e vai sair "Eu sou o filho".</p>
<p>porque os métodos das classes filho sobrescreveram a classe pai.<br />
isso entretanto, só ocorre quando o método é virtual ( no c++ ) e no<br />
java tem Override.</p>
<p>só que, po, eu tou numa classe 'Gente', como é que ele chama o método<br />
da classe 'Pai' ou 'Filho'? o new não tem nada haver com isso, já que<br />
depois que eu dou o new, caio em um ponteiro de 'Gente' e gente é<br />
sempre gente.</p>
<p>só que como marquei o método como virtual, ele consegue descobrir qual<br />
o tipo de classe que está associada a memória por uma coisa chamada<br />
vTable ( Virtual Method Table ), que é uma tabela de variação de<br />
métodos que é construida pelo compilador no momento que o programa<br />
está sendo gerado, e essa tabela guarda as informações de classe e<br />
parametros para ser disparado quando usada. ( se usar o comando -fdump<br />
do g++ você consegue ver a tabela gerada ), aqui num exemplo simples<br />
deu o seguinte:</p>
<p>d:<br />
+0: pointer to virtual method table of D (for B1)<br />
+4: value of int_in_b1<br />
+8: pointer to virtual method table of D (for B2)<br />
+12: value of int_in_b2<br />
+16: value of int_in_d</p>
<p>isso me diz que o 0 e o 12 (binários: 000000, 001100 ) são ponteiros<br />
para métodos que estão na verdade em outra classe, e acessando esses<br />
ponteiros, que indicam a posição da memória de execução ( não de dados<br />
) ele consegue saber o código que será executado.</p>
<p>e Isso é sobrescrita =)"</p>
<p>e eu:</p>
<p>"<span style="font-family:trebuchet ms, sans-serif;">deixa ver se eu entendi:<br />
em  sobrecarga temos 2 metodos com o mesmo nome que pertencem a mesma classe  e com funções diferentes (certo?)"<br />
<em>- sim!</em><br />
"em sobrescrita temos metodos  com o mesmo nome que pertencem a classes diferentes e que sobrescrevem o  método da classe pai com o mesmo nome. se o metdodo da classe filha nao  é virtual, qdo chamado ele vai executar o metodo da classe pai?</span>"<br />
<em>- sim!</em></p>
<p>Valeu @tumaix.</p>
<p>inté.</p>,-
author: Camila
categories: Archives, Personal/Pessoal, poo, Programming
date: "2010-04-20T13:31:26Z"

published: true
status: publish
tags: poo, Programming
title: Sobrecarga != Sobrescrita


<p>Em um rápido lapso de raciocínio você também chegou a pensar que sobecarga é a mesma coisa que sobrescrita?<br />
Calma, que o @tumaix te explica:</p>
<p>"Sobrecarga é uma coisa, Sobrescrita é outra.</p>
<p>Sobrecarga:<br />
Métodos na mesma classe, com nome igual e argumentos diferentes.</p>
<p>ex., imagina que você tem 4 classes, 'Jogador', 'Mesa', 'Baralho' e<br />
'Carta', aonde o Baralho tem que dar cartas a mesa e Jogador. em<br />
Linguagens que não tem sobrecarga, você recisa fazer algo como</p>
<p>Class BaralhoSemSobrecarga{<br />
void daCartasJogador(Jogador j);<br />
void daCartasMesa(Mesa m);<br />
};</p>
<p>só a assinatura. Mas poxa, a 'Razão de ser' de ambos os métodos é um<br />
só, que é dar cartas. dai veio a idéia de sobrecarga, que é fazer um<br />
jeito dos métodos existirem com mesmo nome, mas funcionarem de forma<br />
diferente:</p>
<p>Class BaralhoComSobrecarga{<br />
void daCartas(Jogador j);<br />
void daCartas(Mesa m);<br />
}</p>
<p>como os tipos utilizados dentro do método são diferentes, o compilador<br />
constroi o método para ser invocado pelo nome + tipo de parametro<br />
passado ( descoberto pelo comando typeid() ), e só então chama o<br />
método correto. isso é bem bom pra manter a coerência do programa.</p>
<p>Já sobrescrita é quando você cria um método em uma classe:<br />
class Gente{<br />
virtual void falar(){ std::cout &lt;&lt; "Eu sou gente" };<br />
}<br />
class Pai : public Gente{<br />
void falar(){ std::cout &lt;&lt; "Oi, eu sou o pai"; }<br />
}<br />
class Filho : public Gente{<br />
void falar(){std::cout &lt;&lt; "Oi eu sou o filho"; }<br />
}</p>
<p>temos 3 classes, bem pequenas, só pra comparar.</p>
<p>Gente *a = new Gente();<br />
Gente *b = new Pai();<br />
Gente *c = new Filho();</p>
<p>eu criei 3 objetos do tipo 'Gente', só que dois dele são subclasses.<br />
isso significa que eu posso fazer<br />
a-&gt;falar() e vai sair "Eu sou gente";<br />
b-&gt; falar() e vai sair "Eu sou o pai";<br />
c-&gt; falar() e vai sair "Eu sou o filho".</p>
<p>porque os métodos das classes filho sobrescreveram a classe pai.<br />
isso entretanto, só ocorre quando o método é virtual ( no c++ ) e no<br />
java tem Override.</p>
<p>só que, po, eu tou numa classe 'Gente', como é que ele chama o método<br />
da classe 'Pai' ou 'Filho'? o new não tem nada haver com isso, já que<br />
depois que eu dou o new, caio em um ponteiro de 'Gente' e gente é<br />
sempre gente.</p>
<p>só que como marquei o método como virtual, ele consegue descobrir qual<br />
o tipo de classe que está associada a memória por uma coisa chamada<br />
vTable ( Virtual Method Table ), que é uma tabela de variação de<br />
métodos que é construida pelo compilador no momento que o programa<br />
está sendo gerado, e essa tabela guarda as informações de classe e<br />
parametros para ser disparado quando usada. ( se usar o comando -fdump<br />
do g++ você consegue ver a tabela gerada ), aqui num exemplo simples<br />
deu o seguinte:</p>
<p>d:<br />
+0: pointer to virtual method table of D (for B1)<br />
+4: value of int_in_b1<br />
+8: pointer to virtual method table of D (for B2)<br />
+12: value of int_in_b2<br />
+16: value of int_in_d</p>
<p>isso me diz que o 0 e o 12 (binários: 000000, 001100 ) são ponteiros<br />
para métodos que estão na verdade em outra classe, e acessando esses<br />
ponteiros, que indicam a posição da memória de execução ( não de dados<br />
) ele consegue saber o código que será executado.</p>
<p>e Isso é sobrescrita =)"</p>
<p>e eu:</p>
<p>"<span style="font-family:trebuchet ms, sans-serif;">deixa ver se eu entendi:<br />
em  sobrecarga temos 2 metodos com o mesmo nome que pertencem a mesma classe  e com funções diferentes (certo?)"<br />
<em>- sim!</em><br />
"em sobrescrita temos metodos  com o mesmo nome que pertencem a classes diferentes e que sobrescrevem o  método da classe pai com o mesmo nome. se o metdodo da classe filha nao  é virtual, qdo chamado ele vai executar o metodo da classe pai?</span>"<br />
<em>- sim!</em></p>
<p>Valeu @tumaix.</p>,-
author: Camila
categories: Archives, Personal/Pessoal, poo, Programming
date: "2010-04-20T13:31:26Z"

published: true
status: publish
tags: poo, Programming
title: Sobrecarga != Sobrescrita


<p>Em um rápido lapso de raciocínio você também chegou a pensar que sobecarga é a mesma coisa que sobrescrita?<br />
Calma, que o @tumaix te explica:</p>
<p>"Sobrecarga é uma coisa, Sobrescrita é outra.</p>
<p>Sobrecarga:<br />
Métodos na mesma classe, com nome igual e argumentos diferentes.</p>
<p>ex., imagina que você tem 4 classes, 'Jogador', 'Mesa', 'Baralho' e<br />
'Carta', aonde o Baralho tem que dar cartas a mesa e Jogador. em<br />
Linguagens que não tem sobrecarga, você recisa fazer algo como</p>
<p>Class BaralhoSemSobrecarga{<br />
void daCartasJogador(Jogador j);<br />
void daCartasMesa(Mesa m);<br />
};</p>
<p>só a assinatura. Mas poxa, a 'Razão de ser' de ambos os métodos é um<br />
só, que é dar cartas. dai veio a idéia de sobrecarga, que é fazer um<br />
jeito dos métodos existirem com mesmo nome, mas funcionarem de forma<br />
diferente:</p>
<p>Class BaralhoComSobrecarga{<br />
void daCartas(Jogador j);<br />
void daCartas(Mesa m);<br />
}</p>
<p>como os tipos utilizados dentro do método são diferentes, o compilador<br />
constroi o método para ser invocado pelo nome + tipo de parametro<br />
passado ( descoberto pelo comando typeid() ), e só então chama o<br />
método correto. isso é bem bom pra manter a coerência do programa.</p>
<p>Já sobrescrita é quando você cria um método em uma classe:<br />
class Gente{<br />
virtual void falar(){ std::cout &lt;&lt; "Eu sou gente" };<br />
}<br />
class Pai : public Gente{<br />
void falar(){ std::cout &lt;&lt; "Oi, eu sou o pai"; }<br />
}<br />
class Filho : public Gente{<br />
void falar(){std::cout &lt;&lt; "Oi eu sou o filho"; }<br />
}</p>
<p>temos 3 classes, bem pequenas, só pra comparar.</p>
<p>Gente *a = new Gente();<br />
Gente *b = new Pai();<br />
Gente *c = new Filho();</p>
<p>eu criei 3 objetos do tipo 'Gente', só que dois dele são subclasses.<br />
isso significa que eu posso fazer<br />
a-&gt;falar() e vai sair "Eu sou gente";<br />
b-&gt; falar() e vai sair "Eu sou o pai";<br />
c-&gt; falar() e vai sair "Eu sou o filho".</p>
<p>porque os métodos das classes filho sobrescreveram a classe pai.<br />
isso entretanto, só ocorre quando o método é virtual ( no c++ ) e no<br />
java tem Override.</p>
<p>só que, po, eu tou numa classe 'Gente', como é que ele chama o método<br />
da classe 'Pai' ou 'Filho'? o new não tem nada haver com isso, já que<br />
depois que eu dou o new, caio em um ponteiro de 'Gente' e gente é<br />
sempre gente.</p>
<p>só que como marquei o método como virtual, ele consegue descobrir qual<br />
o tipo de classe que está associada a memória por uma coisa chamada<br />
vTable ( Virtual Method Table ), que é uma tabela de variação de<br />
métodos que é construida pelo compilador no momento que o programa<br />
está sendo gerado, e essa tabela guarda as informações de classe e<br />
parametros para ser disparado quando usada. ( se usar o comando -fdump<br />
do g++ você consegue ver a tabela gerada ), aqui num exemplo simples<br />
deu o seguinte:</p>
<p>d:<br />
+0: pointer to virtual method table of D (for B1)<br />
+4: value of int_in_b1<br />
+8: pointer to virtual method table of D (for B2)<br />
+12: value of int_in_b2<br />
+16: value of int_in_d</p>
<p>isso me diz que o 0 e o 12 (binários: 000000, 001100 ) são ponteiros<br />
para métodos que estão na verdade em outra classe, e acessando esses<br />
ponteiros, que indicam a posição da memória de execução ( não de dados<br />
) ele consegue saber o código que será executado.</p>
<p>e Isso é sobrescrita =)"</p>
<p>e eu:</p>
<p>"<span style="font-family:trebuchet ms, sans-serif;">deixa ver se eu entendi:<br />
em  sobrecarga temos 2 metodos com o mesmo nome que pertencem a mesma classe  e com funções diferentes (certo?)"<br />
<em>- sim!</em><br />
"em sobrescrita temos metodos  com o mesmo nome que pertencem a classes diferentes e que sobrescrevem o  método da classe pai com o mesmo nome. se o metdodo da classe filha nao  é virtual, qdo chamado ele vai executar o metodo da classe pai?</span>"<br />
<em>- sim!</em></p>
<p>Valeu @tumaix.</p>,-
author: Camila
categories: Archives, Personal/Pessoal, poo, Programming
date: "2010-04-20T13:31:26Z"

published: true
status: publish
tags: poo, Programming
title: Sobrecarga != Sobrescrita


<p>Em um rápido lapso de raciocínio você também chegou a pensar que sobecarga é a mesma coisa que sobrescrita?<br />
Calma, que o @tumaix te explica:</p>
<p>"Sobrecarga é uma coisa, Sobrescrita é outra.</p>
<p>Sobrecarga:<br />
Métodos na mesma classe, com nome igual e argumentos diferentes.</p>
<p>ex., imagina que você tem 4 classes, 'Jogador', 'Mesa', 'Baralho' e<br />
'Carta', aonde o Baralho tem que dar cartas a mesa e Jogador. em<br />
Linguagens que não tem sobrecarga, você recisa fazer algo como</p>
<p>Class BaralhoSemSobrecarga{<br />
void daCartasJogador(Jogador j);<br />
void daCartasMesa(Mesa m);<br />
};</p>
<p>só a assinatura. Mas poxa, a 'Razão de ser' de ambos os métodos é um<br />
só, que é dar cartas. dai veio a idéia de sobrecarga, que é fazer um<br />
jeito dos métodos existirem com mesmo nome, mas funcionarem de forma<br />
diferente:</p>
<p>Class BaralhoComSobrecarga{<br />
void daCartas(Jogador j);<br />
void daCartas(Mesa m);<br />
}</p>
<p>como os tipos utilizados dentro do método são diferentes, o compilador<br />
constroi o método para ser invocado pelo nome + tipo de parametro<br />
passado ( descoberto pelo comando typeid() ), e só então chama o<br />
método correto. isso é bem bom pra manter a coerência do programa.</p>
<p>Já sobrescrita é quando você cria um método em uma classe:<br />
class Gente{<br />
virtual void falar(){ std::cout &lt;&lt; "Eu sou gente" };<br />
}<br />
class Pai : public Gente{<br />
void falar(){ std::cout &lt;&lt; "Oi, eu sou o pai"; }<br />
}<br />
class Filho : public Gente{<br />
void falar(){std::cout &lt;&lt; "Oi eu sou o filho"; }<br />
}</p>
<p>temos 3 classes, bem pequenas, só pra comparar.</p>
<p>Gente *a = new Gente();<br />
Gente *b = new Pai();<br />
Gente *c = new Filho();</p>
<p>eu criei 3 objetos do tipo 'Gente', só que dois dele são subclasses.<br />
isso significa que eu posso fazer<br />
a-&gt;falar() e vai sair "Eu sou gente";<br />
b-&gt; falar() e vai sair "Eu sou o pai";<br />
c-&gt; falar() e vai sair "Eu sou o filho".</p>
<p>porque os métodos das classes filho sobrescreveram a classe pai.<br />
isso entretanto, só ocorre quando o método é virtual ( no c++ ) e no<br />
java tem Override.</p>
<p>só que, po, eu tou numa classe 'Gente', como é que ele chama o método<br />
da classe 'Pai' ou 'Filho'? o new não tem nada haver com isso, já que<br />
depois que eu dou o new, caio em um ponteiro de 'Gente' e gente é<br />
sempre gente.</p>
<p>só que como marquei o método como virtual, ele consegue descobrir qual<br />
o tipo de classe que está associada a memória por uma coisa chamada<br />
vTable ( Virtual Method Table ), que é uma tabela de variação de<br />
métodos que é construida pelo compilador no momento que o programa<br />
está sendo gerado, e essa tabela guarda as informações de classe e<br />
parametros para ser disparado quando usada. ( se usar o comando -fdump<br />
do g++ você consegue ver a tabela gerada ), aqui num exemplo simples<br />
deu o seguinte:</p>
<p>d:<br />
+0: pointer to virtual method table of D (for B1)<br />
+4: value of int_in_b1<br />
+8: pointer to virtual method table of D (for B2)<br />
+12: value of int_in_b2<br />
+16: value of int_in_d</p>
<p>isso me diz que o 0 e o 12 (binários: 000000, 001100 ) são ponteiros<br />
para métodos que estão na verdade em outra classe, e acessando esses<br />
ponteiros, que indicam a posição da memória de execução ( não de dados<br />
) ele consegue saber o código que será executado.</p>
<p>e Isso é sobrescrita =)"</p>
<p>e eu:</p>
<p>"<span style="font-family:trebuchet ms, sans-serif;">deixa ver se eu entendi:<br />
em  sobrecarga temos 2 metodos com o mesmo nome que pertencem a mesma classe  e com funções diferentes (certo?)"<br />
<em>- sim!</em><br />
"em sobrescrita temos metodos  com o mesmo nome que pertencem a classes diferentes e que sobrescrevem o  método da classe pai com o mesmo nome. se o metdodo da classe filha nao  é virtual, qdo chamado ele vai executar o metodo da classe pai?</span>"<br />
<em>- sim!</em></p>
<p>Valeu @tumaix.</p>
<p>inté.</p>,-
author: Camila
categories: Archives, Personal/Pessoal, poo, Programming
date: "2010-04-20T13:31:26Z"

published: true
status: publish
tags: poo, Programming
title: Sobrecarga != Sobrescrita


<p>Em um rápido lapso de raciocínio você também chegou a pensar que sobecarga é a mesma coisa que sobrescrita?<br />
Calma, que o @tumaix te explica:</p>
<p>"Sobrecarga é uma coisa, Sobrescrita é outra.</p>
<p>Sobrecarga:<br />
Métodos na mesma classe, com nome igual e argumentos diferentes.</p>
<p>ex., imagina que você tem 4 classes, 'Jogador', 'Mesa', 'Baralho' e<br />
'Carta', aonde o Baralho tem que dar cartas a mesa e Jogador. em<br />
Linguagens que não tem sobrecarga, você recisa fazer algo como</p>
<p>Class BaralhoSemSobrecarga{<br />
void daCartasJogador(Jogador j);<br />
void daCartasMesa(Mesa m);<br />
};</p>
<p>só a assinatura. Mas poxa, a 'Razão de ser' de ambos os métodos é um<br />
só, que é dar cartas. dai veio a idéia de sobrecarga, que é fazer um<br />
jeito dos métodos existirem com mesmo nome, mas funcionarem de forma<br />
diferente:</p>
<p>Class BaralhoComSobrecarga{<br />
void daCartas(Jogador j);<br />
void daCartas(Mesa m);<br />
}</p>
<p>como os tipos utilizados dentro do método são diferentes, o compilador<br />
constroi o método para ser invocado pelo nome + tipo de parametro<br />
passado ( descoberto pelo comando typeid() ), e só então chama o<br />
método correto. isso é bem bom pra manter a coerência do programa.</p>
<p>Já sobrescrita é quando você cria um método em uma classe:<br />
class Gente{<br />
virtual void falar(){ std::cout &lt;&lt; "Eu sou gente" };<br />
}<br />
class Pai : public Gente{<br />
void falar(){ std::cout &lt;&lt; "Oi, eu sou o pai"; }<br />
}<br />
class Filho : public Gente{<br />
void falar(){std::cout &lt;&lt; "Oi eu sou o filho"; }<br />
}</p>
<p>temos 3 classes, bem pequenas, só pra comparar.</p>
<p>Gente *a = new Gente();<br />
Gente *b = new Pai();<br />
Gente *c = new Filho();</p>
<p>eu criei 3 objetos do tipo 'Gente', só que dois dele são subclasses.<br />
isso significa que eu posso fazer<br />
a-&gt;falar() e vai sair "Eu sou gente";<br />
b-&gt; falar() e vai sair "Eu sou o pai";<br />
c-&gt; falar() e vai sair "Eu sou o filho".</p>
<p>porque os métodos das classes filho sobrescreveram a classe pai.<br />
isso entretanto, só ocorre quando o método é virtual ( no c++ ) e no<br />
java tem Override.</p>
<p>só que, po, eu tou numa classe 'Gente', como é que ele chama o método<br />
da classe 'Pai' ou 'Filho'? o new não tem nada haver com isso, já que<br />
depois que eu dou o new, caio em um ponteiro de 'Gente' e gente é<br />
sempre gente.</p>
<p>só que como marquei o método como virtual, ele consegue descobrir qual<br />
o tipo de classe que está associada a memória por uma coisa chamada<br />
vTable ( Virtual Method Table ), que é uma tabela de variação de<br />
métodos que é construida pelo compilador no momento que o programa<br />
está sendo gerado, e essa tabela guarda as informações de classe e<br />
parametros para ser disparado quando usada. ( se usar o comando -fdump<br />
do g++ você consegue ver a tabela gerada ), aqui num exemplo simples<br />
deu o seguinte:</p>
<p>d:<br />
+0: pointer to virtual method table of D (for B1)<br />
+4: value of int_in_b1<br />
+8: pointer to virtual method table of D (for B2)<br />
+12: value of int_in_b2<br />
+16: value of int_in_d</p>
<p>isso me diz que o 0 e o 12 (binários: 000000, 001100 ) são ponteiros<br />
para métodos que estão na verdade em outra classe, e acessando esses<br />
ponteiros, que indicam a posição da memória de execução ( não de dados<br />
) ele consegue saber o código que será executado.</p>
<p>e Isso é sobrescrita =)"</p>
<p>e eu:</p>
<p>"<span style="font-family:trebuchet ms, sans-serif;">deixa ver se eu entendi:<br />
em  sobrecarga temos 2 metodos com o mesmo nome que pertencem a mesma classe  e com funções diferentes (certo?)"<br />
<em>- sim!</em><br />
"em sobrescrita temos metodos  com o mesmo nome que pertencem a classes diferentes e que sobrescrevem o  método da classe pai com o mesmo nome. se o metdodo da classe filha nao  é virtual, qdo chamado ele vai executar o metodo da classe pai?</span>"<br />
<em>- sim!</em></p>
<p>Valeu @tumaix.</p>
<p>inté.</p>,-
author: Camila
categories: Archives, Personal/Pessoal, poo, Programming
date: "2010-04-20T13:31:26Z"

published: true
status: publish
tags: poo, Programming
title: Sobrecarga != Sobrescrita


<p>Em um rápido lapso de raciocínio você também chegou a pensar que sobecarga é a mesma coisa que sobrescrita?<br />
Calma, que o @tumaix te explica:</p>
<p>"Sobrecarga é uma coisa, Sobrescrita é outra.</p>
<p>Sobrecarga:<br />
Métodos na mesma classe, com nome igual e argumentos diferentes.</p>
<p>ex., imagina que você tem 4 classes, 'Jogador', 'Mesa', 'Baralho' e<br />
'Carta', aonde o Baralho tem que dar cartas a mesa e Jogador. em<br />
Linguagens que não tem sobrecarga, você recisa fazer algo como</p>
<p>Class BaralhoSemSobrecarga{<br />
void daCartasJogador(Jogador j);<br />
void daCartasMesa(Mesa m);<br />
};</p>
<p>só a assinatura. Mas poxa, a 'Razão de ser' de ambos os métodos é um<br />
só, que é dar cartas. dai veio a idéia de sobrecarga, que é fazer um<br />
jeito dos métodos existirem com mesmo nome, mas funcionarem de forma<br />
diferente:</p>
<p>Class BaralhoComSobrecarga{<br />
void daCartas(Jogador j);<br />
void daCartas(Mesa m);<br />
}</p>
<p>como os tipos utilizados dentro do método são diferentes, o compilador<br />
constroi o método para ser invocado pelo nome + tipo de parametro<br />
passado ( descoberto pelo comando typeid() ), e só então chama o<br />
método correto. isso é bem bom pra manter a coerência do programa.</p>
<p>Já sobrescrita é quando você cria um método em uma classe:<br />
class Gente{<br />
virtual void falar(){ std::cout &lt;&lt; "Eu sou gente" };<br />
}<br />
class Pai : public Gente{<br />
void falar(){ std::cout &lt;&lt; "Oi, eu sou o pai"; }<br />
}<br />
class Filho : public Gente{<br />
void falar(){std::cout &lt;&lt; "Oi eu sou o filho"; }<br />
}</p>
<p>temos 3 classes, bem pequenas, só pra comparar.</p>
<p>Gente *a = new Gente();<br />
Gente *b = new Pai();<br />
Gente *c = new Filho();</p>
<p>eu criei 3 objetos do tipo 'Gente', só que dois dele são subclasses.<br />
isso significa que eu posso fazer<br />
a-&gt;falar() e vai sair "Eu sou gente";<br />
b-&gt; falar() e vai sair "Eu sou o pai";<br />
c-&gt; falar() e vai sair "Eu sou o filho".</p>
<p>porque os métodos das classes filho sobrescreveram a classe pai.<br />
isso entretanto, só ocorre quando o método é virtual ( no c++ ) e no<br />
java tem Override.</p>
<p>só que, po, eu tou numa classe 'Gente', como é que ele chama o método<br />
da classe 'Pai' ou 'Filho'? o new não tem nada haver com isso, já que<br />
depois que eu dou o new, caio em um ponteiro de 'Gente' e gente é<br />
sempre gente.</p>
<p>só que como marquei o método como virtual, ele consegue descobrir qual<br />
o tipo de classe que está associada a memória por uma coisa chamada<br />
vTable ( Virtual Method Table ), que é uma tabela de variação de<br />
métodos que é construida pelo compilador no momento que o programa<br />
está sendo gerado, e essa tabela guarda as informações de classe e<br />
parametros para ser disparado quando usada. ( se usar o comando -fdump<br />
do g++ você consegue ver a tabela gerada ), aqui num exemplo simples<br />
deu o seguinte:</p>
<p>d:<br />
+0: pointer to virtual method table of D (for B1)<br />
+4: value of int_in_b1<br />
+8: pointer to virtual method table of D (for B2)<br />
+12: value of int_in_b2<br />
+16: value of int_in_d</p>
<p>isso me diz que o 0 e o 12 (binários: 000000, 001100 ) são ponteiros<br />
para métodos que estão na verdade em outra classe, e acessando esses<br />
ponteiros, que indicam a posição da memória de execução ( não de dados<br />
) ele consegue saber o código que será executado.</p>
<p>e Isso é sobrescrita =)"</p>
<p>e eu:</p>
<p>"<span style="font-family:trebuchet ms, sans-serif;">deixa ver se eu entendi:<br />
em  sobrecarga temos 2 metodos com o mesmo nome que pertencem a mesma classe  e com funções diferentes (certo?)"<br />
<em>- sim!</em><br />
"em sobrescrita temos metodos  com o mesmo nome que pertencem a classes diferentes e que sobrescrevem o  método da classe pai com o mesmo nome. se o metdodo da classe filha nao  é virtual, qdo chamado ele vai executar o metodo da classe pai?</span>"<br />
<em>- sim!</em></p>
<p>Valeu @tumaix.</p>,-
author: Camila
categories: Archives, Personal/Pessoal, poo, Programming
date: "2010-04-20T13:31:26Z"

published: true
status: publish
tags: poo, Programming
title: Sobrecarga != Sobrescrita


<p>Em um rápido lapso de raciocínio você também chegou a pensar que sobecarga é a mesma coisa que sobrescrita?<br />
Calma, que o @tumaix te explica:</p>
<p>"Sobrecarga é uma coisa, Sobrescrita é outra.</p>
<p>Sobrecarga:<br />
Métodos na mesma classe, com nome igual e argumentos diferentes.</p>
<p>ex., imagina que você tem 4 classes, 'Jogador', 'Mesa', 'Baralho' e<br />
'Carta', aonde o Baralho tem que dar cartas a mesa e Jogador. em<br />
Linguagens que não tem sobrecarga, você recisa fazer algo como</p>
<p>Class BaralhoSemSobrecarga{<br />
void daCartasJogador(Jogador j);<br />
void daCartasMesa(Mesa m);<br />
};</p>
<p>só a assinatura. Mas poxa, a 'Razão de ser' de ambos os métodos é um<br />
só, que é dar cartas. dai veio a idéia de sobrecarga, que é fazer um<br />
jeito dos métodos existirem com mesmo nome, mas funcionarem de forma<br />
diferente:</p>
<p>Class BaralhoComSobrecarga{<br />
void daCartas(Jogador j);<br />
void daCartas(Mesa m);<br />
}</p>
<p>como os tipos utilizados dentro do método são diferentes, o compilador<br />
constroi o método para ser invocado pelo nome + tipo de parametro<br />
passado ( descoberto pelo comando typeid() ), e só então chama o<br />
método correto. isso é bem bom pra manter a coerência do programa.</p>
<p>Já sobrescrita é quando você cria um método em uma classe:<br />
class Gente{<br />
virtual void falar(){ std::cout &lt;&lt; "Eu sou gente" };<br />
}<br />
class Pai : public Gente{<br />
void falar(){ std::cout &lt;&lt; "Oi, eu sou o pai"; }<br />
}<br />
class Filho : public Gente{<br />
void falar(){std::cout &lt;&lt; "Oi eu sou o filho"; }<br />
}</p>
<p>temos 3 classes, bem pequenas, só pra comparar.</p>
<p>Gente *a = new Gente();<br />
Gente *b = new Pai();<br />
Gente *c = new Filho();</p>
<p>eu criei 3 objetos do tipo 'Gente', só que dois dele são subclasses.<br />
isso significa que eu posso fazer<br />
a-&gt;falar() e vai sair "Eu sou gente";<br />
b-&gt; falar() e vai sair "Eu sou o pai";<br />
c-&gt; falar() e vai sair "Eu sou o filho".</p>
<p>porque os métodos das classes filho sobrescreveram a classe pai.<br />
isso entretanto, só ocorre quando o método é virtual ( no c++ ) e no<br />
java tem Override.</p>
<p>só que, po, eu tou numa classe 'Gente', como é que ele chama o método<br />
da classe 'Pai' ou 'Filho'? o new não tem nada haver com isso, já que<br />
depois que eu dou o new, caio em um ponteiro de 'Gente' e gente é<br />
sempre gente.</p>
<p>só que como marquei o método como virtual, ele consegue descobrir qual<br />
o tipo de classe que está associada a memória por uma coisa chamada<br />
vTable ( Virtual Method Table ), que é uma tabela de variação de<br />
métodos que é construida pelo compilador no momento que o programa<br />
está sendo gerado, e essa tabela guarda as informações de classe e<br />
parametros para ser disparado quando usada. ( se usar o comando -fdump<br />
do g++ você consegue ver a tabela gerada ), aqui num exemplo simples<br />
deu o seguinte:</p>
<p>d:<br />
+0: pointer to virtual method table of D (for B1)<br />
+4: value of int_in_b1<br />
+8: pointer to virtual method table of D (for B2)<br />
+12: value of int_in_b2<br />
+16: value of int_in_d</p>
<p>isso me diz que o 0 e o 12 (binários: 000000, 001100 ) são ponteiros<br />
para métodos que estão na verdade em outra classe, e acessando esses<br />
ponteiros, que indicam a posição da memória de execução ( não de dados<br />
) ele consegue saber o código que será executado.</p>
<p>e Isso é sobrescrita =)"</p>
<p>e eu:</p>
<p>"<span style="font-family:trebuchet ms, sans-serif;">deixa ver se eu entendi:<br />
em  sobrecarga temos 2 metodos com o mesmo nome que pertencem a mesma classe  e com funções diferentes (certo?)"<br />
<em>- sim!</em><br />
"em sobrescrita temos metodos  com o mesmo nome que pertencem a classes diferentes e que sobrescrevem o  método da classe pai com o mesmo nome. se o metdodo da classe filha nao  é virtual, qdo chamado ele vai executar o metodo da classe pai?</span>"<br />
<em>- sim!</em></p>
<p>Valeu @tumaix.</p>
<p>inté.</p>,-
author: Camila
categories: Archives, Personal/Pessoal, poo, Programming
date: "2010-04-20T13:31:26Z"

published: true
status: publish
tags: poo, Programming
title: Sobrecarga != Sobrescrita


<p>Em um rápido lapso de raciocínio você também chegou a pensar que sobecarga é a mesma coisa que sobrescrita?<br />
Calma, que o @tumaix te explica:</p>
<p>"Sobrecarga é uma coisa, Sobrescrita é outra.</p>
<p>Sobrecarga:<br />
Métodos na mesma classe, com nome igual e argumentos diferentes.</p>
<p>ex., imagina que você tem 4 classes, 'Jogador', 'Mesa', 'Baralho' e<br />
'Carta', aonde o Baralho tem que dar cartas a mesa e Jogador. em<br />
Linguagens que não tem sobrecarga, você recisa fazer algo como</p>
<p>Class BaralhoSemSobrecarga{<br />
void daCartasJogador(Jogador j);<br />
void daCartasMesa(Mesa m);<br />
};</p>
<p>só a assinatura. Mas poxa, a 'Razão de ser' de ambos os métodos é um<br />
só, que é dar cartas. dai veio a idéia de sobrecarga, que é fazer um<br />
jeito dos métodos existirem com mesmo nome, mas funcionarem de forma<br />
diferente:</p>
<p>Class BaralhoComSobrecarga{<br />
void daCartas(Jogador j);<br />
void daCartas(Mesa m);<br />
}</p>
<p>como os tipos utilizados dentro do método são diferentes, o compilador<br />
constroi o método para ser invocado pelo nome + tipo de parametro<br />
passado ( descoberto pelo comando typeid() ), e só então chama o<br />
método correto. isso é bem bom pra manter a coerência do programa.</p>
<p>Já sobrescrita é quando você cria um método em uma classe:<br />
class Gente{<br />
virtual void falar(){ std::cout &lt;&lt; "Eu sou gente" };<br />
}<br />
class Pai : public Gente{<br />
void falar(){ std::cout &lt;&lt; "Oi, eu sou o pai"; }<br />
}<br />
class Filho : public Gente{<br />
void falar(){std::cout &lt;&lt; "Oi eu sou o filho"; }<br />
}</p>
<p>temos 3 classes, bem pequenas, só pra comparar.</p>
<p>Gente *a = new Gente();<br />
Gente *b = new Pai();<br />
Gente *c = new Filho();</p>
<p>eu criei 3 objetos do tipo 'Gente', só que dois dele são subclasses.<br />
isso significa que eu posso fazer<br />
a-&gt;falar() e vai sair "Eu sou gente";<br />
b-&gt; falar() e vai sair "Eu sou o pai";<br />
c-&gt; falar() e vai sair "Eu sou o filho".</p>
<p>porque os métodos das classes filho sobrescreveram a classe pai.<br />
isso entretanto, só ocorre quando o método é virtual ( no c++ ) e no<br />
java tem Override.</p>
<p>só que, po, eu tou numa classe 'Gente', como é que ele chama o método<br />
da classe 'Pai' ou 'Filho'? o new não tem nada haver com isso, já que<br />
depois que eu dou o new, caio em um ponteiro de 'Gente' e gente é<br />
sempre gente.</p>
<p>só que como marquei o método como virtual, ele consegue descobrir qual<br />
o tipo de classe que está associada a memória por uma coisa chamada<br />
vTable ( Virtual Method Table ), que é uma tabela de variação de<br />
métodos que é construida pelo compilador no momento que o programa<br />
está sendo gerado, e essa tabela guarda as informações de classe e<br />
parametros para ser disparado quando usada. ( se usar o comando -fdump<br />
do g++ você consegue ver a tabela gerada ), aqui num exemplo simples<br />
deu o seguinte:</p>
<p>d:<br />
+0: pointer to virtual method table of D (for B1)<br />
+4: value of int_in_b1<br />
+8: pointer to virtual method table of D (for B2)<br />
+12: value of int_in_b2<br />
+16: value of int_in_d</p>
<p>isso me diz que o 0 e o 12 (binários: 000000, 001100 ) são ponteiros<br />
para métodos que estão na verdade em outra classe, e acessando esses<br />
ponteiros, que indicam a posição da memória de execução ( não de dados<br />
) ele consegue saber o código que será executado.</p>
<p>e Isso é sobrescrita =)"</p>
<p>e eu:</p>
<p>"<span style="font-family:trebuchet ms, sans-serif;">deixa ver se eu entendi:<br />
em  sobrecarga temos 2 metodos com o mesmo nome que pertencem a mesma classe  e com funções diferentes (certo?)"<br />
<em>- sim!</em><br />
"em sobrescrita temos metodos  com o mesmo nome que pertencem a classes diferentes e que sobrescrevem o  método da classe pai com o mesmo nome. se o metdodo da classe filha nao  é virtual, qdo chamado ele vai executar o metodo da classe pai?</span>"<br />
<em>- sim!</em></p>
<p>Valeu @tumaix.</p>
<p>inté.</p>
