const API = 'http://localhost:8000';

function j(el){ return document.getElementById(el); }

async function api(path, opts={}){
  const res = await fetch(API + path, { headers: { 'Content-Type': 'application/json' }, ...opts });
  if(!res.ok){ throw new Error(await res.text()); }
  return res.json();
}

// Users
j('btn_create_user').onclick = async () => {
  const body = { name: j('u_name').value, role: j('u_role').value };
  const out = await api('/api/users', { method:'POST', body: JSON.stringify(body) });
  const all = await api('/api/users');
  j('users_out').textContent = JSON.stringify(all, null, 2);
};

// Memories
j('btn_add_memory').onclick = async () => {
  const body = { patient_id: Number(j('m_pid').value), title: j('m_title').value, content: j('m_content').value };
  const out = await api('/api/memories', { method:'POST', body: JSON.stringify(body) });
  j('mem_out').textContent = JSON.stringify(out, null, 2);
};
j('btn_list_memory').onclick = async () => {
  const pid = Number(j('m_pid').value);
  const out = await api('/api/memories?patient_id=' + pid);
  j('mem_out').textContent = JSON.stringify(out, null, 2);
};

// Reminders
j('btn_add_rem').onclick = async () => {
  const body = { patient_id: Number(j('r_pid').value), text: j('r_text').value, time: new Date(j('r_time').value).toISOString() };
  const out = await api('/api/reminders', { method:'POST', body: JSON.stringify(body) });
  j('rem_out').textContent = JSON.stringify(out, null, 2);
};
j('btn_list_rem').onclick = async () => {
  const pid = Number(j('r_pid').value);
  const out = await api('/api/reminders?patient_id=' + pid);
  j('rem_out').textContent = JSON.stringify(out, null, 2);
};

// Chat
j('btn_send_chat').onclick = async () => {
  const pid = Number(j('c_pid').value);
  const msg = j('c_msg').value;
  const box = j('chat_box');
  const me = document.createElement('div'); me.className = 'msg me'; me.textContent = 'You: ' + msg; box.appendChild(me);
  const out = await api('/api/chat', { method:'POST', body: JSON.stringify({ patient_id: pid, message: msg }) });
  const ai = document.createElement('div'); ai.className = 'msg ai'; ai.textContent = 'AI: ' + out.reply + '  [' + out.sentiment + ']'; box.appendChild(ai);
};
