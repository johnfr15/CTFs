<?php

$path = $_GET['path'] ?? '';
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Serveur de fichiers ASTRA</title>
    <style>

        body {
            background: linear-gradient(135deg, #1a2a6c, #b21f1f, #fdbb2d);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #fff;
            margin: 0;
            padding: 0;
            min-height: 100vh; 

        }
        .container {
            max-width: 800px;
            margin: 80px auto;
            padding: 20px;
            background-color: rgba(0, 0, 0, 0.6);
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.5);
        }
        h1, h2 {
            text-align: center;
        }
        p {
            text-align: center;
            font-size: 1.2em;
        }
        .content {
            background: #fff;
            color: #333;
            margin: 20px auto;
            padding: 15px;
            border-radius: 8px;
            max-width: 90%;
            word-wrap: break-word;
        }
        .doc-list {
            margin: 20px auto;
            max-width: 90%;
            text-align: center;
        }
        .doc-list a {
            display: inline-block;
            margin: 10px;
            padding: 10px 20px;
            background: #1a2a6c;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            transition: background 0.3s ease;
        }
        .doc-list a:hover {
            background: #b21f1f;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Bienvenue sur le serveur de l'agence ASTRA</h1>
        
        <?php 
        $baseDir = "/var/www/html/";

        if (!empty($path)) : 
            $decodedPath = urldecode($path);
            $decodedPath = str_replace("../", "", $decodedPath);
            $fullPath = realpath($baseDir . $decodedPath);

            if (is_dir($fullPath)) {

                echo "<h2>Contenu du dossier " . htmlspecialchars($decodedPath, ENT_QUOTES, 'UTF-8') . "</h2>";
                echo "<div class='content'><ul>";

                $files = scandir($fullPath);
                foreach ($files as $file) {
                    if ($file !== "." && $file !== "..") {
                        echo "<li>$file</li>";
                    }
                }
                echo "</ul></div>";
            } elseif (is_file($fullPath)) {

                echo "<h2>Contenu du fichier " . htmlspecialchars($decodedPath, ENT_QUOTES, 'UTF-8') . "</h2>";
                echo "<div class='content'>";
                include($fullPath);
                echo "</div>";
                
            } else {
                echo "<h2>Fichier ou dossier introuvable</h2>";
            }
        ?>
        <div class="doc-list" style="text-align: center; margin-top: 20px;">
            <button onclick="window.location.href='?'" style="padding: 10px 20px; background: #1a2a6c; color: #fff; border: none; border-radius: 5px; cursor: pointer;">
                Retour
            </button>
        </div>
        <?php else : ?>
            <p>Naviguez parmi les documents de mission déclassifiés ci-dessous :</p>
            <div class="doc-list">
                <a href="?path=doc1.txt">Document 1 - Hélios</a>
                <a href="?path=doc2.txt">Document 2 - Pioneer</a>
                <a href="?path=doc3.txt">Document 3 - Apophis</a>
                <a href="?path=doc4.txt">Document 4 - Titan</a>
                <a href="?path=doc5.txt">Document 5 - Orbital Polaris</a>
                <a href="?path=doc6.txt">Document 6 - SolarShield</a>
                <a href="?path=doc7.txt">Document 7 - Odyssey</a>
                <a href="?path=doc8.txt">Document 8 - Kepler-442b</a>
                <a href="?path=doc9.txt">Document 9 - Europa DeepDive</a>
                <a href="?path=doc10.txt">Document 10 - Event Horizon</a>
                <a href="?path=doc11.txt">Document 11 - Anomalie X-17</a>
            </div>
        <?php endif; ?>
        
    </div>
</body>
</html>
