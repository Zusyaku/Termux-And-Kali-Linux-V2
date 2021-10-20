package cli

import (
	"log"
	"os"
	"strings"

	"github.com/blackcrw/wafi/cli/cmd"
	"github.com/blackcrw/wafi/internal"
	"github.com/blackcrw/wafi/pkg/nettools"
	"github.com/spf13/cobra"
)

var root = &cobra.Command{
	Use:     "wafi",
	Short:   "WAFI",
	Long:    internal.TextBanner() + `WAFI (Web Application Firewall / Intrusion)`,
	Run:     cmd.RootCMDRun,
	PostRun: cmd.RootCMDPostRun,
}

func init() {
	cobra.OnInitialize(checks_lists)

	root.PersistentFlags().StringP("url", "u", "", "Target URL (Ex: http(s)://example.com/). ")

	root.MarkPersistentFlagRequired("url")
}

func checks_lists() {
	var target, _ = root.Flags().GetString("url")

	internal.SimpleBanner()

	if !strings.HasSuffix(target, "/") { target = target + "/" }
	if !nettools.NetTools_URLValidate(target) { log.Fatalln("This is URL not validate") }
}

func Execute() {
	if err := root.Execute(); err != nil {
		os.Exit(0)
	}
}
