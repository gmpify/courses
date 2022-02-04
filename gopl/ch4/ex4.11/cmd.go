package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"os/exec"

	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
	Use:   "issues",
	Short: "issues is a CLI for handling GH Issues",
	Run: func(cmd *cobra.Command, args []string) {
		// Do Stuff Here
	},
}

var createCmd = &cobra.Command{
	Use:   "create",
	Short: "Create issue",
	Run: func(cmd *cobra.Command, args []string) {
		owner := cmd.Flags().Lookup("owner").Value.String()
		repo := cmd.Flags().Lookup("repo").Value.String()
		fmt.Printf("Creating issue on %s/%s\n", owner, repo)

		fmt.Print("Title for the issue: ")
		reader := bufio.NewReader(os.Stdin)
		title, err := reader.ReadString('\n')
		if err != nil {
			fmt.Println(err)
		}

		f, err := ioutil.TempFile("/tmp", "ex411")
		if err != nil {
			fmt.Println(err)
		}
		filename := f.Name()
		defer os.Remove(filename)

		f.WriteString("This is your issue body. Replace with whatever content you prefer.\n")
		f.Close()
		txtEditor := exec.Command("vim", filename)
		txtEditor.Stdout = os.Stdout
		txtEditor.Stdin = os.Stdin
		txtEditor.Stderr = os.Stderr
		txtEditor.Run()

		dat, err := os.ReadFile(filename)
		if err != nil {
			fmt.Println(err)
		}

		err = CreateIssue(owner, repo, title, string(dat))
		if err != nil {
			fmt.Println(err)
		}
	},
}

var readCmd = &cobra.Command{
	Use:   "read",
	Short: "Read issues",
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("Hugo Static Site Generator v0.9 -- HEAD")
	},
}

func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}

func init() {
	rootCmd.PersistentFlags().StringP("owner", "o", "", "Github owner of the repository")
	rootCmd.PersistentFlags().StringP("repo", "r", "", "Github repository")

	rootCmd.MarkPersistentFlagRequired("owner")
	rootCmd.MarkPersistentFlagRequired("repo")

	rootCmd.AddCommand(readCmd)
	rootCmd.AddCommand(createCmd)
}
