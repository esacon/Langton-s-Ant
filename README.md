# Langton-s-Ant
Langton's Ant made with Python.
<p>Una hormiga se mueve en una grilla, conformada por cuadrados o celdas que pueden ser blancas o negras. La hormiga está siempre orientada en alguna de las direcciones cardinales (izquierda, derecha, arriba o abajo) y se mueve de una celda a cualquiera de las adyacentes de acuerdo a las siguientes reglas:</p>
<ul>
<li><p>Si está en una celda negra, cambia el color de esa celda a blanco, rota 90 grados en dirección opuesta a las manecillas del reloj y avanza una celda.</p></li>
<li><p>Si está en una celda blanca, cambia el color de la celda a negro, rota 90 grados en el sentido de las manecillas del reloj y avanza una celda.</p></li>
</ul>
<p>Dadas estas reglas básicas, haga un programa en Python que permita elegir el tamaño de la grilla, un número <em>N</em> de movimientos y una posición inicial <span class="math inline">\((x_0,y_0)\)</span>. Y, que a partir de esto, muestre el estado del tablero (incluyendo la hormiga y la dirrección a la que apunta) en la iteración <em>N</em>.</p>
