### ---
# title: "RMS Letter Comparison"
# author: "Wm Salt Hale"
# date: "March 25, 2021"
# license: "GPL-3"
## ---

# Clean Workspace
rm(list = ls())

# Global Variables
gen_plots_toggle <- FALSE

# Load Libraries
required_pkgs <- c("here", "tidyverse", "scales")
installed_pkgs <- installed.packages()
sapply(required_pkgs, function(p) {
  if(!p %in% installed_pkgs[,1]) {
    install.packages(p)
  }
})
# https://stackoverflow.com/questions/8175912/load-multiple-packages-at-once/8176099#8176099
lapply(required_pkgs, require, character.only = TRUE)

here::i_am('code/01-process_data.R')
here()

# Helper Functions
source(here('code', '99_helpers.R'))

# Load Data
df <- read.csv(here('data', 'rms-letter-signers.csv'))
#df <- readRDS(here('data', 'dataset.Rds'))
#df_facts <- readRDS(here('data', 'facts.Rds'))

# Drop Unused Columns
df$ID <- df$NodeID <- df$Gravatar <- df$Collaborators <- df$Inviter <- 
  df$PrivateGists <- df$PrivateRepos <- df$OwnedPrivateRepos <- 
  df$Plan <- df$Role <- df$TeamCount <- df$Type <- df$DiskUsage <- 
  df$URL <- df$FollowersURL <- df$FollowingURL <- df$ReposURL <- 
  df$StarredURL <-df$GistsURL <- df$htmlURL <- df$EventsURL <-
  df$OrganizationsURL <- df$InvitationTeamsURL <- df$ReceivedEventsURL <- df$SubscriptionsURL <-
  NULL

# initialize facts list, collect original state
df_facts <- list()

# Store facts
df_facts$orig_total_signers <- length(df$Username)
df_facts$orig_rr_signers <- length(df$Username[df$Repo == 'rr'])
df_facts$orig_sr_signers <- length(df$Username[df$Repo == 'sr'])

df <- df %>%
  mutate(AccountAge = as.numeric(difftime(Updated, Created), units='weeks'))

df_rr <- df[df$Repo == 'rr',]
df_sr <- df[df$Repo == 'sr',]

df_facts$total_with_name <- length(df$Username[df$Name != ''])
df_facts$rr_with_name <- length(df_rr$Username[df_rr$Name != ''])
df_facts$sr_with_name <- length(df_sr$Username[df_sr$Name != ''])

df_facts$total_with_bio <- length(df$Username[df$Bio != ''])
df_facts$rr_with_bio <- length(df_rr$Username[df_rr$Bio != ''])
df_facts$sr_with_bio <- length(df_sr$Username[df_sr$Bio != ''])

df_facts$total_with_blog <- length(df$Username[df$Blog != ''])
df_facts$rr_with_blog <- length(df_rr$Username[df_rr$Blog != ''])
df_facts$sr_with_blog <- length(df_sr$Username[df_sr$Blog != ''])

df_facts$total_with_email <- length(df$Username[df$Email != ''])
df_facts$rr_with_email <- length(df_rr$Username[df_rr$Email != ''])
df_facts$sr_with_email <- length(df_sr$Username[df_sr$Email != ''])

df_facts$total_with_twitter <- length(df$Username[df$Twitter != ''])
df_facts$rr_with_twitter <- length(df_rr$Username[df_rr$Twitter != ''])
df_facts$sr_with_twitter <- length(df_sr$Username[df_sr$Twitter != ''])

df_facts$total_with_company <- length(df$Username[df$Company != ''])
df_facts$rr_with_company <- length(df_rr$Username[df_rr$Company != ''])
df_facts$sr_with_company <- length(df_sr$Username[df_sr$Company != ''])

df_facts$total_unique_companies <- length(unique(df$Company[df$Company != '']))
df_facts$rr_unique_companies <- length(unique(df_rr$Company[df_rr$Company != '']))
df_facts$sr_unique_companies <- length(unique(df_sr$Company[df_sr$Company != '']))

df_facts$total_mean_account_age <- mean(df$AccountAge)
df_facts$rr_mean_account_age <- mean(df_rr$AccountAge)
df_facts$sr_mean_account_age <- mean(df_sr$AccountAge)

df_facts$total_median_account_age <- median(df$AccountAge)
df_facts$rr_median_account_age <- median(df_rr$AccountAge)
df_facts$sr_median_account_age <- median(df_sr$AccountAge)

df_facts$total_mean_public_repos <- mean(df$PublicRepos)
df_facts$rr_mean_public_repos <- mean(df_rr$PublicRepos)
df_facts$sr_mean_public_repos <- mean(df_sr$PublicRepos)

df_facts$total_median_public_repos <- median(df$PublicRepos)
df_facts$rr_median_public_repos <- median(df_rr$PublicRepos)
df_facts$sr_median_public_repos <- median(df_sr$PublicRepos)

df_facts$total_mean_public_gists <- mean(df$PublicGists)
df_facts$rr_mean_public_gists <- mean(df_rr$PublicGists)
df_facts$sr_mean_public_gists <- mean(df_sr$PublicGists)

df_facts$total_median_public_gists <- median(df$PublicGists)
df_facts$rr_median_public_gists <- median(df_rr$PublicGists)
df_facts$sr_median_public_gists <- median(df_sr$PublicGists)

df_facts$total_mean_followers <- mean(df$Followers)
df_facts$rr_mean_followers <- mean(df_rr$Followers)
df_facts$sr_mean_followers <- mean(df_sr$Followers)

df_facts$total_median_followers <- median(df$Followers)
df_facts$rr_median_followers <- median(df_rr$Followers)
df_facts$sr_median_followers <- median(df_sr$Followers)

df_facts$total_mean_following <- mean(df$Following)
df_facts$rr_mean_following <- mean(df_rr$Following)
df_facts$sr_mean_following <- mean(df_sr$Following)

df_facts$total_median_following <- median(df$Following)
df_facts$rr_median_following <- median(df_rr$Following)
df_facts$sr_median_following <- median(df_sr$Following)

# Percentages
df_facts$total_percentage_with_name <- 100 * (length(df$Username[df$Name != '']) / df_facts$orig_total_signers)
df_facts$rr_percentage_with_name <- 100 * (length(df_rr$Username[df_rr$Name != '']) / df_facts$orig_rr_signers)
df_facts$sr_percentage_with_name <- 100 * (length(df_sr$Username[df_sr$Name != '']) / df_facts$orig_sr_signers)

df_facts$total_percentage_with_bio <- 100 * (length(df$Username[df$Bio != '']) / df_facts$orig_total_signers)
df_facts$rr_percentage_with_bio <- 100 * (length(df_rr$Username[df_rr$Bio != '']) / df_facts$orig_rr_signers)
df_facts$sr_percentage_with_bio <- 100 * (length(df_sr$Username[df_sr$Bio != '']) / df_facts$orig_sr_signers)

df_facts$total_percentage_with_blog <- 100 * (length(df$Username[df$Blog != '']) / df_facts$orig_total_signers)
df_facts$rr_percentage_with_blog <- 100 * (length(df_rr$Username[df_rr$Blog != '']) / df_facts$orig_rr_signers)
df_facts$sr_percentage_with_blog <- 100 * (length(df_sr$Username[df_sr$Blog != '']) / df_facts$orig_sr_signers)

df_facts$total_percentage_with_email <- 100 * (length(df$Username[df$Email != '']) / df_facts$orig_total_signers)
df_facts$rr_percentage_with_email <- 100 * (length(df_rr$Username[df_rr$Email != '']) / df_facts$orig_rr_signers)
df_facts$sr_percentage_with_email <- 100 * (length(df_sr$Username[df_sr$Email != '']) / df_facts$orig_sr_signers)

df_facts$total_percentage_with_twitter <- 100 * (length(df$Username[df$Twitter != '']) / df_facts$orig_total_signers)
df_facts$rr_percentage_with_twitter <- 100 * (length(df_rr$Username[df_rr$Twitter != '']) / df_facts$orig_rr_signers)
df_facts$sr_percentage_with_twitter <- 100 * (length(df_sr$Username[df_sr$Twitter != '']) / df_facts$orig_sr_signers)

df_facts$total_percentage_with_company <- 100 * (length(df$Username[df$Company != '']) / df_facts$orig_total_signers)
df_facts$rr_percentage_with_company <- 100 * (length(df_rr$Username[df_rr$Company != '']) / df_facts$orig_rr_signers)
df_facts$sr_percentage_with_company <- 100 * (length(df_sr$Username[df_sr$Company != '']) / df_facts$orig_sr_signers)


# Save datasets
saveRDS(df, file=here('data', 'dataset.Rds'))
saveRDS(df_facts, file=here('data', 'facts.Rds'))
#saveRDS(df_tables, file=here('data', 'tables.Rds'))
