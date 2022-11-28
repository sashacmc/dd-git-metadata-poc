package com.datadoghq.gitmetadatapoc;

import datadog.trace.api.Trace;

/**
 * Trace sample 
 *
 */
public class App 
{
    @Trace(operationName = "main", resourceName = "app")
    public static void main( String[] args )
    {
        System.out.println( "Trace sample" );
        throw new ArithmeticException( "Some exception" );
    }
}
