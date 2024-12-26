<script>
    import { onMount } from "svelte";

    let linkedListInput = ''; // User input
    let steps = [];           // Steps returned from backend
    let isLoading = false;    // Loading state
    let result = null;        // Result of palindrome check

    const checkPalindrome = async () => {
        // Parse user input into a list of integers
        const list = linkedListInput
            .split(",")
            .map(val => parseInt(val.trim(), 10));

        // Reset states
        isLoading = true;
        steps = [];
        result = null;

        try {
            const response = await fetch("http://localhost:8000/check_palindrome", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(list),
            });

            if (!response.ok) {
                throw new Error("Failed to check palindrome.");
            }

            const data = await response.json();
            steps = data.steps || [];
            result = data.is_palindrome; 
        } catch (error) {
            console.error("Error:", error.message);
            result = null;
        } finally {
            isLoading = false;
        }
    };
</script>

<main class="hero bg-base-200 min-h-screen">
    <div class="hero-content text-center flex-col">
        <div class="max-w-md">
            <h1 class="text-3xl font-semibold text-center text-primary mb-4">
                Palindrome Linked List Checker
            </h1>
        
            <label for="linkedList" class="text-lg font-medium text-center text-accent mb-2">
                Enter linked list values (comma-separated):
            </label>
            <input
              type="text"
              id="linkedList"
              bind:value={linkedListInput}
              placeholder="1, 2, 2, 1"
              class="input input-secondary m-4 text-center focus:outline-none focus:ring-2 focus:ring-purple-600"
            />
          
           
        
        
          
        </div>
        <button
            on:click={checkPalindrome}
            disabled={isLoading}
            class="btn btn-primary disabled:bg-gray-400 transition-all duration-300"
        >
            {#if isLoading}
            Checking...
            {:else}
            Check Palindrome
            {/if}
      </button>
        <div class="hero-content w-max-content flex-col mt-4">
            {#if isLoading}
          <div class="w-8 h-8 border-4 border-t-4 border-purple-600 rounded-full animate-spin mt-4"></div>
            {/if}
        
            {#if steps.length > 0}
            <div class="mt-4 p-4 w-max-content bg-base-200 border rounded-lg shadow-lg">
                {#each steps as step, index (step.node)}
                <div class="flex justify-between mb-2">
                    <div class="text-xl font-semibold text-accent p-4">
                    Node: {step.node}
                    </div>
                    <div class="text-xl font-semibold text-accent p-4">
                    Stack Top: {step.stack_top}
                    </div>
                    <div
                    class={`text-xl font-semibold p-4 ${step.is_palindrome ? 'text-success' : 'text-error'}`}
                    >
                    {step.is_palindrome ? 'Palindrome' : 'Not Palindrome'}
                    </div>
                </div>
                {/each}
            </div>
            {/if}
            
            {#if result !== null}
                <p
                  class="mt-4 text-2xl font-bold text-center p-2 rounded-md transition-all duration-500
                    {result ? 'text-success' : ' text-error'}"
                >
                  The list is {result ? 'a palindrome' : 'not a palindrome'}!
                </p>
            {/if}
        </div>
        </div>
</main>


