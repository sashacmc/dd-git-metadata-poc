package main

import (
	"errors"
	"fmt"
	"gopkg.in/DataDog/dd-trace-go.v1/ddtrace/tracer"
)

func main() {
	tracer.Start(
		tracer.WithService("gitmetadatapoc"),
		tracer.WithEnv("dev"),
	)
	defer tracer.Stop()

	span := tracer.StartSpan("main", tracer.ResourceName("/gitmetadatapoc"))
	defer func() {
		span.Finish(tracer.WithError(errors.New("some error")))
		fmt.Println("send span")
	}()

	fmt.Println("gitmetadatapoc runs")
}
