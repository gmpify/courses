package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)

const IssuesURL = "https://api.github.com"

type Issue struct {
	Number  int    `json:",omitempty"`
	HTMLURL string `json:"html_url,omitempty"`
	Title   string `json:"title"`
	State   string `json:",omitempty"`
	Body    string `json:"body"`
}

func CreateIssue(owner, repo, title, body string) error {
	requestBody, err := json.Marshal(Issue{Title: title, Body: body})
	if err != nil {
		return err
	}

	createURL := IssuesURL + fmt.Sprintf("/repos/%s/%s/issues", owner, repo)
	request, err := http.NewRequest("POST", createURL, bytes.NewBuffer(requestBody))
	if err != nil {
		return err
	}

	request.Header.Set("Accept", "application/vnd.github.v3+json")
	request.Header.Set("Content-Type", "application/json")
	request.Header.Set("Authorization", fmt.Sprintf("token %s", os.Getenv("GITHUB_TOKEN")))

	client := http.Client{}
	resp, err := client.Do(request)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusCreated {
		return fmt.Errorf("failted to create issue: %s", resp.Status)
	}

	return nil
}
