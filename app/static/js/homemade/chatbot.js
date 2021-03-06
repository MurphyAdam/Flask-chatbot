var ChatBot = {


    RenderBotMessage: function({data, direction} = {}) {
      if (data){
        if(direction === "sent"){
          if (data.sent)
          {
              return ` 
                  <div class='media is-marginless is-borderless' style='padding-top: 0;'><div class='media-content is-marginless'><div class='content'>\
                   <div class='notification is-marginless message-container-right-branch ${data.category} animated pulse' style='padding: 0.8rem !important;'>\
                   <div>${data.sent}</div></div><span class="is-0-8rem">Now</span></div></div><div class='media-right'><figure class='image is-32x32'>\
                   <img class='is-rounded' src='https://www.gravatar.com/avatar/?d=monsterid'></figure></div></div>
                   `;
          }
        }
        else if(direction === "received") {
          if (data.response)
            {
              return ` 
                   <div class='media is-marginless is-borderless' style='padding-top: 0;'>\
                   <div class='media-left'><figure class='image is-32x32'>\
                   <img class='is-rounded' src='https://www.gravatar.com/avatar/5beb6288b37391868418d8d212b35db0?d=identicon&s=64'></figure></div><div class='media-content is-marginless'>\
                   <div class='content'><div class='notification is-marginless message-container-left-branch is-info animated pulse' style='padding: 0.8rem !important;'>\
                   <div>${data.response}</div></div><span class="is-0-8rem">Now</span></div></div></div>
                  `;  
            }       
        }
      }
      else {
        return false;
      }
    },


    sendBotMessage: function() {
      $('#sendBotMessageForm').submit(function(event) {
        event.preventDefault();
        var $this = $(this);
        let dataToSend = $this.serialize();
        $this['0']['2'].placeholder="Waiting for response...";
        $('#sendBotMessageForm')['0'].reset();
      $.post('/chatbot/chat', dataToSend
        ).done(function(data) {
        $("#chatBotInnerContainer").append(ChatBot.RenderBotMessage({data:data, direction:"sent"}));
        $("#chatBotInnerContainer").append(ChatBot.RenderBotMessage({data:data, direction:"received"}));
        $('#chatBotContainer').scrollTop($('#chatBotContainer')['0'].scrollHeight);
      }).fail(function(jqXHR, textStatus) {
          Swal.fire({
            title: textStatus,
            text: 'An error occured. Please check your network and try again',
            icon: 'error',
            showClass: {
              popup: 'animated fadeInDown'
            },
            hideClass: {
              popup: 'animated fadeOutUp'
            },
            confirmButtonText: 'Okay'
          });
      }).always(function(){
        $this['0']['2'].placeholder="Write something";
      });
      return false;
      });
    },


      init: function(){
        ChatBot.RenderBotMessage();
        ChatBot.sendBotMessage();
      }


};

$(document).ready(ChatBot.init());