package com.internship.emaildigest.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import java.util.Map;
import java.util.HashMap;
import java.util.List;

@Service
public class AiServiceClient {

    @Value("${ai.service.url:http://localhost:5000}")
    private String aiServiceUrl;

    private final RestTemplate restTemplate;

    public AiServiceClient() {
        org.springframework.http.client.SimpleClientHttpRequestFactory factory = new org.springframework.http.client.SimpleClientHttpRequestFactory();
        factory.setConnectTimeout(10000);
        factory.setReadTimeout(10000);
        this.restTemplate = new RestTemplate(factory);
    }

    public Map<String, Object> describeEmail(String emailBody) {
        String url = aiServiceUrl + "/api/v1/ai/describe";
        Map<String, String> request = new HashMap<>();
        request.put("email_body", emailBody);

        try {
            return restTemplate.postForObject(url, request, Map.class);
        } catch (Exception e) {
            System.err.println("Error calling AI describe: " + e.getMessage());
            return null;
        }
    }

    public List<Map<String, Object>> recommendActions(String description, Double sentiment) {
        String url = aiServiceUrl + "/api/v1/ai/recommend";
        Map<String, Object> request = new HashMap<>();
        request.put("description", description);
        request.put("sentiment", sentiment);

        try {
            return restTemplate.postForObject(url, request, List.class);
        } catch (Exception e) {
            System.err.println("Error calling AI recommend: " + e.getMessage());
            return null;
        }
    }

    public Map<String, Object> generateReport(List<String> summaries) {
        String url = aiServiceUrl + "/api/v1/ai/generate-report";
        Map<String, Object> request = new HashMap<>();
        request.put("summaries", summaries);

        try {
            return restTemplate.postForObject(url, request, Map.class);
        } catch (Exception e) {
            System.err.println("Error calling AI generate-report: " + e.getMessage());
            return null;
        }
    }
}
