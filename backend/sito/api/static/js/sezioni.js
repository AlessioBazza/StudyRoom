
    <% for(var i = 0; i < data.length; i++) { %>
        <div style="padding:10px;margin:5px 0px 5px 0px;border:1px solid gray;" id="<%= data[i].id %>">
            <ul>
            <li><b>nome:</b><%= data[i].nome %></li>
                <li><b>ultimo aggiornamento:</b><%= data[i].ultimo_aggiornamento || "mai" %></li>
                    <li><b>media posti:</b><%= data[i].stat.media || "-" %></li>
                        </ul>

                    <b>Report:</b>
                    <input type="text" id="report-<%= data[i].id %>" value=""></input>
                    <a href="#" onclick="submit_posti(<%= data[i].id %>);">Submit</a>
                    </div>
                    <% } %>
