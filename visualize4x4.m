%POMDP simulation visualization

belief = belief4x4(:,1:end-1);
[r,c] = size(belief);
start = 1;
stop = 100;
fps = 1;
saveVideo = 0;
saveImages = 1;
endFrames = 3;
clear M
j=1;
if saveVideo
    writerObj = VideoWriter('4x4.avi');
    writerObj.FrameRate = fps;
    open(writerObj);
end
for i = start:min(stop,r)
    b1 = belief(i,:);
    b1 = b1-min(min(b1));
    b1 = b1/norm(b1);
    bgrid = flipud(vec2mat(b1,4))
    imagesc(bgrid); 
    colormap(flipud(colormap('gray')));
    axis square
    M(j) = getframe;
    
    if saveVideo
        writeVideo(writerObj,M(j));
    elseif saveImages
        fname = sprintf('4x4_%d_.jpg',i);
        I = M(j).cdata;
        imwrite(I,fname);
    end
    j=j+1;
end
if saveVideo
    for i = 1:endFrames
        writeVideo(writerObj,M(j-1));
    end
    close(writerObj);
end
% movie(M,1,fps)

