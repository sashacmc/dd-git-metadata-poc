require "ddtrace"

require "ddtrace/auto_instrument"

def get_commit_sha
  `git rev-parse HEAD 2>/dev/null`.strip
rescue StandardError
end

def get_repository_url
  `git config --get remote.origin.url 2>/dev/null`.strip
rescue StandardError
end

Datadog.configure do |c|
  c.tags = { "git.commit.sha" => get_commit_sha(),
             "git.repository_url" => get_repository_url() }
end

Datadog::Tracing.trace("gitmetadatapoc", resource: "main-resource") do |span|
  puts "gitmetadatapoc runs"
end
