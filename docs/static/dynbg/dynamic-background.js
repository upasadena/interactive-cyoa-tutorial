/**
 * dynamic-background.js
 *
 * This script dynamically allows you to dynamically change your background
 * colour and/or image using <div>'s and CSS id's.
 *
 * Made by /u/_pasadena
 */

/**
 * MIT License
 *
 * Copyright (c) 2023 Pasadena
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to
 * deal in the Software without restriction, including without limitation the
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE.
 */

/**
 * CONSTANTS
 * 
 * Change these as needed
 */
// Change to true if there is a bug
const DEBUG = false;
// The amount of pixels from the centre that determine where the threshold for
// transitioning is
const centerThreshold = 45; // pixels

// Whether a background colour should be set by default
const setDefaultBackground = true;
// Id in the css: `#red: { background: #900; }`
const defaultBackgroundId = "red";
// END CONSTANTS

function lastElement(arr) {
  let returnValue = null;

  if (setDefaultBackground) {
    returnValue = defaultBackgroundId;
  }

  return arr ? arr.slice(-1) : returnValue;
}

function isFullArray(arr) {
  return arr && arr.length >= 1;
}

function debugObject(obj) {
  console.log(`${JSON.stringify(obj, undefined, 2)}`);
}

// Anonymous "self-invoking" function
(function() {
  let startingTime = new Date().getTime();
  // Load the script
  let script = document.createElement("script");
  script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js";
  script.type = "text/javascript";
  document.getElementsByTagName("head")[0].appendChild(script);

  // Poll for jQuery to come into existence
  let checkReady = function(callback) {
      if (window.jQuery) {
          callback(jQuery);
      }
      else {
          window.setTimeout(function() { checkReady(callback); }, 20);
      }
  };

  // Start polling...
  checkReady(function($) {
    // "Global" variables
    // let previousBackground = undefined;
    let lastScrollTop = 0;
    let userScrolledDown = false;
    const historyObj = {
      objectsAbove: undefined, // array of strings
      currentObject: undefined ,
    };
    let $previousThis;
    let scrollUpObject;

    if (setDefaultBackground) {
      historyObj.currentObject = defaultBackgroundId;
    }

    if (DEBUG) debugObject(historyObj);

    // This function goes once jQuery is loaded
    $(function() {
      let endingTime = new Date().getTime();
      let tookTime = endingTime - startingTime;
      if (DEBUG) {
        console.log("jQuery is loaded, after " + tookTime + " milliseconds!");
      }

      if (setDefaultBackground) {
        $(".pb-12").addClass(defaultBackgroundId);
        historyObj.currentObject = defaultBackgroundId;
      }
    });

    // Check if the user has scrolled to the top or bottom
    $(function () {
      var $win = $(window);

      $win.scroll(function () {
        if ($win.scrollTop() <= 0) {
          if (DEBUG) console.log("Scrolled to Page Top");
          
          if (setDefaultBackground) {
            if (historyObj.currentObject) {
              $(".pb-12").removeClass(historyObj.currentObject);
            }

            $(".pb-12").addClass(defaultBackgroundId);
            historyObj.currentObject = defaultBackgroundId;
          }
        } else if (
          $win.height() + $win.scrollTop() == $(document).height()
        ) {
          // doesn't work I think
          if (DEBUG) console.log("Scrolled to Page Bottom");
        }
      });
    });

    // Check if the <div> is in the viewport
    $.fn.isInViewport = function() {
      /**
       * The absolute (in the context of the page) y position of the
       * elements, static
       */
      let elementTop = $(this).offset().top;
      let elementBottom = elementTop + $(this).outerHeight();
    
      /**
       * The top and bottom pixels that are seen
       */
      let viewportTop = $(window).scrollTop();
      let viewportBottom = viewportTop + $(window).height();

      // Create center variables
      const viewportCenter =
        viewportTop + ((viewportBottom - viewportTop) / 2);
      const viewportCenterTop = viewportCenter - centerThreshold;
      const viewportCenterBottom = viewportCenter + centerThreshold;
      // Check if it's within the center
      const withinViewportCenter =
        elementBottom > viewportCenterTop &&
        elementTop < viewportCenterBottom;

      return withinViewportCenter;
    };
    
    // Check if the user has scrolled up or down
    $(window).scroll(function(event){
      let st = $(this).scrollTop();

      if (st > lastScrollTop) {
        // If the user scrolled down
        userScrolledDown = true;
      } else {
        // If the user scrolled up
        userScrolledDown = false;
      }

      lastScrollTop = st;
    });
    
    // On scroll
    $(window).on("resize scroll", function() {
      $(".bg").each(function() {
        let activeBackground = $(this).attr("id");
        
        if ($(this).isInViewport()) {
          $previousThis = $(this);

          // If the background hasn't changed, return
          if (historyObj.currentObject === activeBackground) {
            return;
          }

          // If the user scrolled down
          if (userScrolledDown) {
            // If the history object exists and isn't an empty list
            if (isFullArray(historyObj.objectsAbove)) {
              // Push the old currentObject
              historyObj.objectsAbove.push(historyObj.currentObject)
              $(".pb-12").removeClass(historyObj.currentObject);
            } else {
              historyObj.objectsAbove = [historyObj.currentObject];
            }

            historyObj.currentObject = activeBackground;

            if (DEBUG) debugObject(historyObj);

            $(".pb-12").addClass(historyObj.currentObject);

          }
        // If the previous context exists and that div is visible in the
        // viewport, and if the user is scrolling up, then run this
        } else if ($previousThis &&
          $previousThis.isInViewport() &&
          !userScrolledDown) {

          let previousBackground = $previousThis.attr("id");

          if (scrollUpObject && scrollUpObject == previousBackground) {
            return;
          }

          scrollUpObject = previousBackground;
            
          if (historyObj.currentObject == previousBackground ||
            historyObj.currentObject == activeBackground) {

            $(".pb-12").removeClass(historyObj.currentObject);
            historyObj.currentObject = historyObj.objectsAbove.pop();

            if (isFullArray(historyObj.objectsAbove)) {
              $(".pb-12").addClass(historyObj.currentObject);
            } else if (setDefaultBackground) {
              $(".pb-12").addClass(defaultBackgroundId);
            }

            if (DEBUG) console.log(debugObject(historyObj));
          }
        }
      });
    });
  });
})();
