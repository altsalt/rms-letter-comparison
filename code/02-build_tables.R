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
df <- readRDS(here('data', 'dataset.Rds'))
df_facts <- readRDS(here('data', 'facts.Rds'))

# Create empty list to store tables
df_tables <- list()

# Generate facts table
rr_column <- c(df_facts$orig_rr_signers, df_facts$rr_percentage_known,
               df_facts$rr_percentage_anonymous, df_facts$rr_percentage_multiple,
               df_facts$rr_percentage_queried, df_facts$rr_percentage_identified,
               df_facts$rr_percentage_with_name,
               df_facts$rr_percentage_with_bio, df_facts$rr_percentage_with_email,
               df_facts$rr_percentage_with_blog, df_facts$rr_percentage_with_twitter,
               df_facts$rr_percentage_with_company, df_facts$rr_unique_companies,
               df_facts$rr_mean_account_age, df_facts$rr_median_account_age,
               df_facts$rr_mean_public_repos, df_facts$rr_median_public_repos,
               df_facts$rr_mean_public_gists, df_facts$rr_median_public_gists,
               df_facts$rr_mean_followers, df_facts$rr_median_followers,
               df_facts$rr_mean_following, df_facts$rr_median_following)

sr_column <- c(df_facts$orig_sr_signers, df_facts$sr_percentage_known,
               df_facts$sr_percentage_anonymous, df_facts$sr_percentage_multiple,
               df_facts$sr_percentage_queried, df_facts$sr_percentage_identified,
               df_facts$sr_percentage_with_name,
               df_facts$sr_percentage_with_bio, df_facts$sr_percentage_with_email,
               df_facts$sr_percentage_with_blog, df_facts$sr_percentage_with_twitter,
               df_facts$sr_percentage_with_company, df_facts$sr_unique_companies,
               df_facts$sr_mean_account_age, df_facts$sr_median_account_age,
               df_facts$sr_mean_public_repos, df_facts$sr_median_public_repos,
               df_facts$sr_mean_public_gists, df_facts$sr_median_public_gists,
               df_facts$sr_mean_followers, df_facts$sr_median_followers,
               df_facts$sr_mean_following, df_facts$sr_median_following)

total_column <- c(df_facts$orig_total_signers, df_facts$total_percentage_known,
                  df_facts$total_percentage_anonymous, df_facts$total_percentage_multiple,
                  df_facts$total_percentage_queried, df_facts$total_percentage_identified,
                  df_facts$total_percentage_with_name,
                  df_facts$total_percentage_with_bio, df_facts$total_percentage_with_email,
                  df_facts$total_percentage_with_blog, df_facts$total_percentage_with_twitter,
                  df_facts$total_percentage_with_company, df_facts$total_unique_companies,
                  df_facts$total_mean_account_age, df_facts$total_median_account_age,
                  df_facts$total_mean_public_repos, df_facts$total_median_public_repos,
                  df_facts$total_mean_public_gists, df_facts$total_median_public_gists,
                  df_facts$total_mean_followers, df_facts$total_median_followers,
                  df_facts$total_mean_following, df_facts$total_median_following)

facts_table <- data.frame(rr_column, sr_column, total_column)
names(facts_table) <- c('Reject rms', 'Support rms', 'Total')
rownames(facts_table) <- c('Number of Signers', 'Percentage Self Identified',
                           'Percentage Anonymous', 'Percentage with Multiple Potential Identities',
                           'Percentage Identified via Query', 'Percentage Identifiable',
                           'Percentage with Name',
                           'Percentage with Bio', 'Percentage with Email',
                           'Percentage with Blog', 'Percentage with Twitter',
                           'Percentage with Company', 'Total Unique Companies',
                           'Mean Account Age (in weeks)', 'Median Account Age (in weeks)',
                           'Mean Public Repos', 'Median Public Repos',
                           'Mean Public Gists', 'Median Public Gists',
                           'Mean Followers', 'Median Followers',
                           'Mean Following', 'Median Following')

df_tables$facts_table <- facts_table

#saveRDS(df, file=here('data', 'dataset.Rds'))
#saveRDS(df_facts, file=here('data', 'facts.Rds'))
saveRDS(df_tables, file=here('data', 'tables.Rds'))
