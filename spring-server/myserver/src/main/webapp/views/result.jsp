<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Sentiment Analysis Result</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            background-color: #fff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #333;
        }
        .sentiment-info {
            margin-top: 20px;
        }
        .sentiment-info p {
            margin: 10px 0;
        }
        .sentiment-label {
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Sentiment Analysis Result</h2>
        <div class="sentiment-info">
 
            <p><span class="sentiment-label">Message has :</span> ${sentiment.prediction} sentiment.</p>
        </div>
    </div>
</body>
</html>
