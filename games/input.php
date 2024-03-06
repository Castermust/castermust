<?php
// Connessione al database
$servername = "localhost"; // Indirizzo del server
$username = "root"; // Username di default di XAMPP
$password = ""; // Password vuota di default di XAMPP
$dbname = "games"; // Nome del database

// Connessione a MySQL
$conn = new mysqli($servername, $username, $password, $dbname);

// Verifica della connessione
if ($conn->connect_error) {
    die("Connessione fallita: " . $conn->connect_error);
}

// Recupero il valore del campo "game-name" inviato dal modulo HTML
$gameName = $_POST['game-name'];

// Query SQL per l'inserimento del dato nella colonna "game" della tabella "game"
$sql = "INSERT INTO game (game) VALUES ('$gameName')";

// Esecuzione della query
if ($conn->query($sql) === TRUE) {
    echo "Dato inserito correttamente nel database.";
} else {
    echo "Errore durante l'inserimento: " . $conn->error;
}



// Chiusura della connessione
$conn->close();



?>