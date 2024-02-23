
import streamlit as st
from datetime import datetime, timedelta
from PIL import Image
import time

#Gets user input

def app():
    

    # Then, inject a global style override in your app:
    style = """
    <style>
        /* This sets the background for the entire page */
        body {
            background-color: #000000; /* Set the background to black */
        }

        /* Add additional styles as needed */
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)

    
    # Page Configuration
    # Custom CSS to inject into the Streamlit app to center the title
    title_alignment = """
        <style>
        h1 {
            text-align: center;
        }
        </style>
        """

    # Insert the custom CSS with the markdown renderer
    st.markdown(title_alignment, unsafe_allow_html=True)

    if st.sidebar.button("Refresh"):
    # Use Streamlit's session state to trigger a rerun when the button is clicked
        st.session_state['refresh'] = not st.session_state.get('refresh', False)

    c1,c2,c3 = st.columns((3), gap='large')
   
    import streamlit.components.v1 as components
    with c1:
        
       

        # The total time for the stopwatch (in milliseconds)
        total_time_ms = 60 * 1000 * 2  # 5 minutes, for example

        st.title("APAC")
        html_code = f"""
        <style>
        .centered-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }}
        </style>
        <div class="centered-container">
            <div id="clock" style="position: relative; width: 200px; height: 200px; border: 10px solid #333; border-radius: 50%; background-color: #fff;">
                <!-- Clock marks -->
                <div style="position: absolute; width: 100%; height: 100%; border-radius: 50%;">
                    <div style="position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 10%; height: 10%; background-color: #333;"></div>
                    <div style="position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 10%; height: 10%; background-color: #333;"></div>
                    <div style="position: absolute; left: 0; top: 50%; transform: translateY(-50%); width: 10%; height: 10%; background-color: #333;"></div>
                    <div style="position: absolute; right: 0; top: 50%; transform: translateY(-50%); width: 10%; height: 10%; background-color: #333;"></div>
                </div>
                <!-- Clock hand -->
                <div id="hand" style="position: absolute; bottom: 50%; left: 50%; width: 2px; height: 40%; background-color: red; transform-origin: 50% 100%;"></div>
            </div>
        </div>

        <script>
        // Delay start and set total time for the stopwatch
        var delayStart = 1; // 2 minutes in milliseconds
        var totalTime = {total_time_ms}; // Use the Python variable
        var startTime = Date.now() + delayStart;
        var clockHand = document.getElementById('hand');

        function updateClock() {{
            var currentTime = Date.now();
            var elapsedTime = currentTime - startTime;

            // Check if the delay period has passed before starting the clock
            if (elapsedTime > 0) {{
                // Calculate the percentage of the total time that has elapsed
                var percent = (elapsedTime % totalTime) / totalTime;

                // Calculate the angle of the hand
                var angle = percent * 360;

                // Rotate the hand accordingly
                clockHand.style.transform = 'rotate(' + angle + 'deg)';
            }}

            // Continue the loop
            requestAnimationFrame(updateClock);
        }}

        // Initial call to the updateClock function after the delay
        setTimeout(updateClock, delayStart);
        </script>
        """
        # Use Streamlit's components.html to render the HTML/JavaScript
        components.html(html_code, height=300)

    with c2:
        st.title("EUROZONE")
        html_code = f"""
        <style>
        .centered-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }}
        </style>
        <div class="centered-container">
            <div id="clock" style="position: relative; width: 200px; height: 200px; border: 10px solid #333; border-radius: 50%; background-color: #fff;">
                <!-- Clock marks -->
                <div style="position: absolute; width: 100%; height: 100%; border-radius: 50%;">
                    <div style="position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 10%; height: 10%; background-color: #333;"></div>
                    <div style="position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 10%; height: 10%; background-color: #333;"></div>
                    <div style="position: absolute; left: 0; top: 50%; transform: translateY(-50%); width: 10%; height: 10%; background-color: #333;"></div>
                    <div style="position: absolute; right: 0; top: 50%; transform: translateY(-50%); width: 10%; height: 10%; background-color: #333;"></div>
                </div>
                <!-- Clock hand -->
                <div id="hand" style="position: absolute; bottom: 50%; left: 50%; width: 2px; height: 40%; background-color: red; transform-origin: 50% 100%;"></div>
            </div>
        </div>

        <script>
        // Delay start and set total time for the stopwatch
        var delayStart = 2 * 60 * 1000; // 2 minutes in milliseconds
        var totalTime = {total_time_ms}; // Use the Python variable
        var startTime = Date.now() + delayStart;
        var clockHand = document.getElementById('hand');

        function updateClock() {{
            var currentTime = Date.now();
            var elapsedTime = currentTime - startTime;

            // Check if the delay period has passed before starting the clock
            if (elapsedTime > 0) {{
                // Calculate the percentage of the total time that has elapsed
                var percent = (elapsedTime % totalTime) / totalTime;

                // Calculate the angle of the hand
                var angle = percent * 360;

                // Rotate the hand accordingly
                clockHand.style.transform = 'rotate(' + angle + 'deg)';
            }}

            // Continue the loop
            requestAnimationFrame(updateClock);
        }}

        // Initial call to the updateClock function after the delay
        setTimeout(updateClock, delayStart);
        </script>
        """
        # Use Streamlit's components.html to render the HTML/JavaScript
        components.html(html_code, height=300)

    with c3:
        st.title("US")
        html_code = f"""
        <style>
        .centered-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }}
        </style>
        <div class="centered-container">
            <div id="clock" style="position: relative; width: 200px; height: 200px; border: 10px solid #333; border-radius: 50%; background-color: #fff;">
                <!-- Clock marks -->
                <div style="position: absolute; width: 100%; height: 100%; border-radius: 50%;">
                    <div style="position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 10%; height: 10%; background-color: #333;"></div>
                    <div style="position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 10%; height: 10%; background-color: #333;"></div>
                    <div style="position: absolute; left: 0; top: 50%; transform: translateY(-50%); width: 10%; height: 10%; background-color: #333;"></div>
                    <div style="position: absolute; right: 0; top: 50%; transform: translateY(-50%); width: 10%; height: 10%; background-color: #333;"></div>
                </div>
                <!-- Clock hand -->
                <div id="hand" style="position: absolute; bottom: 50%; left: 50%; width: 2px; height: 40%; background-color: red; transform-origin: 50% 100%;"></div>
            </div>
        </div>

        <script>
        // Delay start and set total time for the stopwatch
        var delayStart = 4 * 60 * 1000; // 2 minutes in milliseconds
        var totalTime = {total_time_ms}; // Use the Python variable
        var startTime = Date.now() + delayStart;
        var clockHand = document.getElementById('hand');

        function updateClock() {{
            var currentTime = Date.now();
            var elapsedTime = currentTime - startTime;

            // Check if the delay period has passed before starting the clock
            if (elapsedTime > 0) {{
                // Calculate the percentage of the total time that has elapsed
                var percent = (elapsedTime % totalTime) / totalTime;

                // Calculate the angle of the hand
                var angle = percent * 360;

                // Rotate the hand accordingly
                clockHand.style.transform = 'rotate(' + angle + 'deg)';
            }}

            // Continue the loop
            requestAnimationFrame(updateClock);
        }}

        // Initial call to the updateClock function after the delay
        setTimeout(updateClock, delayStart);
        </script>
        """
        # Use Streamlit's components.html to render the HTML/JavaScript
        components.html(html_code, height=300)

    

    st.sidebar.button("Start trading!", key='strt')
    if st.session_state.strt:

        ticket_details_html = """
        <div id="ticket-details" style="display: none; background-color: #393939; color: white; margin: 20px auto; padding: 20px; width: 90%; max-width: 2500px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); font-family: sans-serif;">
            
            <h3 style="text-align: center;">Ticket Details</h3>

            <div style="display: flex; justify-content: space-between; align-items: center; text-align: center;">
                <div style="flex: 1; margin-right: 80px; margin-left: 80px;">
                    <p>Client: Harris Saunas & Co.</p>
                    <p>Client Payment Type: Low Value Payment</p>
                </div>
                <div style="flex: 1; margin-right: 80px; margin-left: 80px;">
                    <p>Amount USD: $85,000</p>
                    <p>Amount EUR: $100,000</p>
                </div>
                <div style="flex: 1; margin-left: 80px;">
                    <p>Value Date: 2024-02-22</p>
                    <p>Rate: 1 USD = 0.85 EUR</p>
                </div>
            </div>
        </div>
        <script>
            setTimeout(function() {
                document.getElementById('ticket-details').style.display = 'flex';
            }, 5000); // 5000 milliseconds = 5 seconds
        </script>
        """

        # Use Streamlit's components.html to render the HTML content
        components.html(ticket_details_html, height=200)

        ticket_details_html = """
        <div id="ticket-details" style="display: none; background-color: #393939; color: white; margin: 20px auto; padding: 20px; width: 90%; max-width: 2500px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); font-family: sans-serif;">
            
            <h3 style="text-align: center;">Ticket Details</h3>

            <div style="display: flex; justify-content: space-between; align-items: center; text-align: center;">
                <div style="flex: 1; margin-right: 80px; margin-left: 80px;">
                    <p>Client: Owens Epoxy Floors</p>
                    <p>Client Payment Type: Low Value Payment</p>
                </div>
                <div style="flex: 1; margin-right: 80px; margin-left: 80px;">
                    <p>Amount USD: $850</p>
                    <p>Amount EUR: $1,000</p>
                </div>
                <div style="flex: 1; margin-left: 80px;">
                    <p>Value Date: 2024-02-22</p>
                    <p>Rate: 1 EUR = 0.85 USD</p>
                </div>
            </div>
        </div>
        <script>
            setTimeout(function() {
                document.getElementById('ticket-details').style.display = 'flex';
            }, 6000); // 5000 milliseconds = 5 seconds
        </script>
        """

        # Use Streamlit's components.html to render the HTML content
        components.html(ticket_details_html, height=200)

    
        ticket_details_html = """
            <div id="ticket-details" style="display: none; background-color: #393939; color: white; margin: 20px auto; padding: 20px; width: 90%; max-width: 2500px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); font-family: sans-serif;">
                
                <h3 style="text-align: center;">Ticket Details</h3>

                <div style="display: flex; justify-content: space-between; align-items: center; text-align: center;">
                    <div style="flex: 1; margin-right: 80px; margin-left: 80px;">
                        <p>Client: Harris Saunas & Co.</p>
                        <p>Client Payment Type: Low Value Payment</p>
                    </div>
                    <div style="flex: 1; margin-right: 80px; margin-left: 80px;">
                        <p>Amount USD: $850</p>
                        <p>Amount EUR: $1,000</p>
                    </div>
                    <div style="flex: 1; margin-left: 80px;">
                        <p>Value Date: 2024-02-22</p>
                        <p>Rate: 1 USD = 0.85 EUR</p>
                    </div>
                </div>
            </div>
            <script>
                setTimeout(function() {
                    document.getElementById('ticket-details').style.display = 'flex';
                }, 7000); // 5000 milliseconds = 5 seconds
            </script>
            """

            # Use Streamlit's components.html to render the HTML content
        components.html(ticket_details_html, height=200)
