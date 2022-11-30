require 'ddtrace'

require 'ddtrace/auto_instrument'

Datadog::Tracing.trace("gitmetadatapoc", resource: "main-resource") do |span|
	puts "gitmetadatapoc runs"
end
