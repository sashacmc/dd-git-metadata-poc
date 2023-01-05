package main

import (
	"errors"
	"fmt"
	"time"

	"gopkg.in/DataDog/dd-trace-go.v1/ddtrace/tracer"
	"gopkg.in/DataDog/dd-trace-go.v1/profiler"
)

func doSomething() {
	time.Sleep(1500 * time.Millisecond)
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
		profiler.WithUploadTimeout(1*time.Second),
		profiler.WithPeriod(1*time.Second),
		profiler.CPUDuration(1*time.Second),
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
