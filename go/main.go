package main

import (
	"errors"
	"fmt"
	"gopkg.in/DataDog/dd-trace-go.v1/ddtrace/tracer"
	"gopkg.in/DataDog/dd-trace-go.v1/profiler"
	"time"
)

func doSomething() {
	time.Sleep(time.Second)
	fmt.Println("gitmetadatapoc runs")
}

func main() {
	tracer.Start(
		tracer.WithService("gitmetadatapoc"),
		tracer.WithEnv("dev"),
	)
	defer tracer.Stop()

	err := profiler.Start(
		profiler.WithProfileTypes(
			profiler.CPUProfile,
			profiler.HeapProfile,
		),
		profiler.WithService("gitmetadatapoc"),
		profiler.WithEnv("dev"),
	)
	if err != nil {
		fmt.Println(err)
	}
	defer profiler.Stop()

	span := tracer.StartSpan("main", tracer.ResourceName("/gitmetadatapoc"))
	defer func() {
		span.Finish(tracer.WithError(errors.New("some error")))
		fmt.Println("send span")
	}()

	doSomething()
}
