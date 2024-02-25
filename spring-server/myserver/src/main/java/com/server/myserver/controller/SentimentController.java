package com.server.myserver.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.server.myserver.entities.Message;
import com.server.myserver.entities.Sentiment;
import com.server.myserver.service.SentimentService;

// @RestController
// @RequestMapping("/sentiment")
// public class SentimentController {

//     @Autowired
//     private SentimentService service;

//     @PostMapping("/analyze")
//     public ResponseEntity<Sentiment> analyzeSentiment(@RequestBody Message msg) {
//         return ResponseEntity.ok(service.getSentiment(msg));
//     }

// }

@Controller
@RequestMapping("/sentiment")
public class SentimentController {

    @Autowired
    private SentimentService service;

    @PostMapping("/analyze")
    public String analyzeSentiment(@ModelAttribute Message msg, Model model) {
        Sentiment sentiment = service.getSentiment(msg);
        model.addAttribute("sentiment", sentiment);
        return "result";
    }

}