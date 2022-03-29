clear all
close all
op=1;
n=5;
[licz,mian] = pade(op,n);
a=0.4;
b=1;
z1=[];
p1=[-5 -5 -5 -5 -5 -5 -5 -5 -5 -5];
k1=5^10;
sim('modelSimulink2.slx', [0 8]);
figure;
subplot(121)
hold on; 
plot(ans.tout(:,1),ans.simout(:,1),'b');
plot(ans.tout(:,1),ans.simout(:,2),'g');
a=0.8;
b=1;
sim('modelSimulink2.slx',[0 8]);
plot(ans.tout(:,1),ans.simout(:,2),'r');
title('Step response');
xlabel('Time(sec)');
ylabel('Amplitude');
legend('Uklad 10-go rzedu','Uklad 2-go rzedu z opoznieniem a=0.4, b=1','Uklad 2-go rzedu z opoznieniem a=0.8, b=1'); 
hold off; 
subplot(122)
hold on;
plot(ans.tout(:,1),ans.simout(:,1),'b');
plot(ans.tout(:,1),ans.simout(:,2),'g');
a=0.4;
b=1.5;
sim('modelSimulink2.slx',[0 8]);
plot(ans.tout(:,1),ans.simout(:,2),'r');
title('Step response');
xlabel('Time(sec)');
ylabel('Amplitude');
legend('Uklad 10-go rzedu','Uklad 2-go rzedu z opoznieniem a=0.4, b=1','Uklad 2-go rzedu z opoznieniem a=0.4, b=1.5'); 

function e=aproks(x)
global a b licz mian z1 p1 k1
a=x(1);
b=x(2);
op=x(3);
n=5;
[licz,mian] = pade(op,n);
z1=[];
p1=[-5 -5 -5 -5 -5 -5 -5 -5 -5 -5];
k1=5^10;
sim('model2.mdl');
e = sum((simout(:,1)-ans.simout(:,2)).^2);
end 

clear all
close all
global a b licz mian z1 p1 k1
[wynik,c] = fminsearch(@aproks,[1 1 1]);
a = wynik(1)
b = wynik(2)
op = wynik(3)
sim('model2.mdl',[0 8]);
figure;
hold on;
plot(ans.tout(:,1),ans.simout(:,1),'b');
plot(ans.tout(:,1),ans.simout(:,3),'g');
legend('Uklad 10-go rzedu','Uklad 2-go rzedu z opoznieniem');
hold off