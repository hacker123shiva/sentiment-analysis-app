package com.server.myserver.service;

import org.springframework.http.MediaType;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;

import com.server.myserver.entities.Message;
import com.server.myserver.entities.Sentiment;

@Service
public class SentimentService {
    @Autowired
    private RestClient client;

    public Sentiment getSentiment(Message msg) {
        return client.post()
                .uri("/analyze")
                .contentType(MediaType.APPLICATION_JSON)
                .body(msg)
                .retrieve()
                .body(Sentiment.class);
    }
}